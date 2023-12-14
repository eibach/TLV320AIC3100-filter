Purpose
=======
This a tool for calculation filter coefficients for the Texas Instruments [TLV320AIC3100](https://www.ti.com/product//TLV320AIC3100) codec.
There is a vendor tool for this, but it is Windows only, GUI only and not OSS.

This tool is based on scipy and matplotlib. As I clearly have no clue, what I am doing here, please take all results with a grain of salt.

Operation
=========
```
usage: TLV320AIC3100_filters.py [-h] [--lowpass freq] [--highpass freq] [--notch freq bw]

options:
  -h, --help       show this help message and exit
  --lowpass freq
  --highpass freq
  --notch freq bw
```

To generate a filter chain with lowpass, highpass and two notch filters:
```
TLV320AIC3100_filters.py --highpass 200.0 --lowpass 10000 --notch 4000 10 --notch 8000 10
Highpass 200.0 Hz
  1O N0:  0x7e59 N1:  0x81a7 D1:  0x7cb1
Lowpass 10000 Hz
  1O N0:  0x3793 N1:  0x3793 D1:  0x10da
Notch 4000 Hz BW  10 Hz
  BQ N0: 0x7feb N1:  0x9139 N2:  0x7feb D1:  0x6ec7 D2:  0x802b
Notch 8000 Hz BW  10 Hz
  BQ N0: 0x7feb N1:  0xc00b N2:  0x7feb D1:  0x3ff5 D2:  0x802b
```

What is implemented?
====================
- Butterworth first order high- and lowpass
- Notch filter

TODO compared with vendor tool
==============================
- second order Buttwerworth, Linkwitz Riley, Bessel, and variable Q high- and lowpass
- full parametric EQ (frequency, gain, bandwidth)
- shelf filters
- phase shift
