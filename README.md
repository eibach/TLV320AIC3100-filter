Purpose
=======
This a tool for calculation filter coefficients for the Texas Instruments [TLV320AIC3100](https://www.ti.com/product//TLV320AIC3100) codec.
There is a vendor tool for this, but it is Windows only, GUI only and not OSS.

This tool is based on scipy and matplotlib. As I clearly have no clue, what I am doing here, please take all results with a grain of salt.

Operation
=========
```
usage: TLV320AIC3100_filters.py [-h] [--fs freq] [--lowpass freq] [--lowbutter2 freq] [--lowbessel2 freq]
                                [--lowshelf freq  gain] [--highpass freq] [--highbutter2 freq] [--highbessel2 freq]
                                [--highshelf freq  gain] [--notch freq bw] [--peq freq  gain q]

options:
  -h, --help            show this help message and exit
  --fs freq             sampling frequency, must go first, default 48000
  --lowpass freq
  --lowbutter2 freq     second order Butterworth lowpass filter
  --lowbessel2 freq     second order Bessel lowpass filter
  --lowshelf freq  gain
                        second order lowshelving filter
  --highpass freq
  --highbutter2 freq    second order Butterworth highpass filter
  --highbessel2 freq    second order Bessel highpass filter
  --highshelf freq  gain
                        second order highshelving filter
  --notch freq bw
  --peq freq  gain q    Full Parametric EQ
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
- second order Butterworth, and Bessel high- and lowpass
- Notch filter
- full parametric EQ (frequency, gain, bandwidth)
- shelf filters

TODO compared with vendor tool
==============================
- second order Linkwitz Riley and variable Q high- and lowpass
- phase shift
