#!/usr/bin/python3

import argparse
from scipy import signal
import numpy as np
from operator import add
import matplotlib.pyplot as plt

filter_list = []

def one_dot_15(x):
	LSB = 2**-15
	res = round(x / LSB)
	if (res < 0):
		res = 0x10000 + res
	return hex(int(res))

def print_bq(b, a):
	print('  BQ N0:', one_dot_15(b[0]), 'N1: ', one_dot_15(b[1] / 2), 'N2: ', one_dot_15(b[2]), 'D1: ', one_dot_15(-a[1] / 2),  'D2: ', one_dot_15(-a[2]))

def print_1o(b, a):
	print('  1O N0: ', one_dot_15(b[0]), 'N1: ', one_dot_15(b[1]), 'D1: ', one_dot_15(-a[1]))


class LowpassAction(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		print(namespace)
		b, a = signal.butter(1, float(values), btype='low', fs=namespace.fs)
		filter_list.append((b, a))
		print('Lowpass', values, 'Hz')
		print_1o(b, a)

class HighpassAction(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		print(namespace)
		b, a = signal.butter(1, float(values), btype='high', fs=namespace.fs)
		filter_list.append((b, a))
		print('Highpass', values, 'Hz')
		print_1o(b, a)

class NotchAction(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		print(namespace)
		b, a = signal.iirnotch(float(values[0]), float(values[0]) / float(values[1]), fs=namespace.fs)
		filter_list.append((b, a))
		print('Notch', values[0], 'Hz BW ', values[1], 'Hz')
		print_bq(b, a)

parser = argparse.ArgumentParser()

parser.add_argument('--fs', default=48000.0, metavar='freq', type=float, help='sampling frequency, must go first, default 48000')
parser.add_argument('--lowpass', action=LowpassAction, metavar='freq')
parser.add_argument('--highpass', action=HighpassAction, metavar='freq')
parser.add_argument('--notch', action=NotchAction, nargs=2, metavar=('freq', 'bw'))

args = parser.parse_args()

# transformations
amplitudes = np.zeros([19980,])
angles = np.zeros([19980,])

for filter in filter_list:
	(b, a) = filter
	w, h = signal.freqz(b, a, range(20,20000), fs=args.fs)
	amplitudes = amplitudes + (20 * np.log10(abs(h)))
	angles += np.angle(h)

# plot
fig, ax1 = plt.subplots()
fig.canvas.manager.set_window_title('TLV320AIC3100 filter designer')
ax1.set_title('Digital filter frequency response')
ax1.plot(w, amplitudes, 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency')
ax1.set_xscale('log')
ax1.set_ylim(-12, 12)
ax1.set_xticks([100, 1000, 10000], ["100 Hz", "1 kHz", "10 kHz"])
ax1.set_yticks([-12, -9, -6, -3, 0, 3 ,6, 9, 12])
ax1.grid(True, which="both")
ax2 = ax1.twinx()
uwangles = np.unwrap(angles)
ax2.plot(w, uwangles, 'g')
ax2.set_ylabel('Phase', color='g')
ax2.axis('tight')
ax2.set_ylim(-np.pi, np.pi)
ax2.set_yticks([-np.pi, -0.75*np.pi, -0.5*np.pi, -0.25*np.pi, 0, 0.25*np.pi, 0.5*np.pi, 0.75*np.pi, np.pi], ["-180°", "-135°", "-90°", "-45°", "0°", "45°", "90°", "135°", "180°"])
plt.xlim([20, 20000])
plt.show()
