# Software Defined Radio
These are all Digital Signal Processing projects using an SDR, specifically the [RTL SDR](https://www.nooelec.com/store/sdr/sdr-receivers/nesdr-mini.html) and GNURadio.

## Setup and Installation
Assuming you're using APT as a package tool, the following command can install the most recent, stable versions of GNURadio and the package to interface with the RTL-SDR:
```bash
sudo apt install gnuradio gr-osmosdr
```
If you're on another Unix distrubution/operating system, [GNURadio can be installed from source with packages here](https://wiki.gnuradio.org/index.php/InstallingGR) and the same can be done for [Osmocom's package here](https://osmocom.org/projects/gr-osmosdr/wiki). 

To install GQRX for an RF Waterfall plot on Linux, see [their GitHub repo](https://github.com/csete/gqrx).

## Goals
- [X] Implement Frequency Modulation to listen to a radio station
- [X] Extract data transmitted from a vehicle's key fob
- [ ] Listen to GSM Data 
- [ ] Intercept ISS satellite images

## Challenges
Setup and installation of GNURadio was not too challenging; but, to use GNURadio, one must know what frequencies are used to transmit data. Beyond radio stations from ~80 MHz to ~180 Mhz, I was stumped. I was looking for an application that would generate an RF Waterfall plot to identify these tranmission frequencies. I first attempted to use SDR#. On my native linux host, this Windows application seemed to do more harm than good. I eventually stumbled upon [GQRX](https://github.com/csete/gqrx). This is how I was able to find frequencies to intercept.

The Frequency Sink doesn't determine listening frequency; the source block does.


