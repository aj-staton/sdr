# Vehicle Key Fob Data

## The Idea
Wireless key fobs communicate with the recievers in a vehicle to lock/unlock doors, activate the panic alarm, or even start the vehicle. My key (probably made in North America) communicates with the vehicle at ~315 MHz. Data is sent using [frequency-shift keying](https://en.wikipedia.org/wiki/Frequency-shift_keying). In other words, frequency changes correlate to binary on/off signals.

#### How did I know FSK was used?
The two differing frequencies across this FFT are a rather distinctive sign of this form of modulation. 
![FSK Data on a FFT](/key-data/fsk.png)

## If I replicate this signal, can I unlock your car?
No. Vehicle manufacturers have implemented a rolling code as a form of encryption. Meaning, the signal changes slightly each time. If you were to jam my transmitted signal, then send your own replicated signal based off of that jam, then yes. In that case, my car would be unlocked. 

## Challenges
**How do I identify the signal I care about??**
* Taking the magnitude of some real & imaginary complex vector seemed to be a good way to find when data was actively being tranmitted.

**I needed a FIR filter; but, GNURadio's Filter Design Tool wouldn't work.**
* I went to GitHub and searched GNURadio's issues. Sure enough, someone else had an identical issue. I downloaded the source from their repo, then isolated the Design Tool's script. It's attempted execution returned dependancy issues with [PyQTGraph](www.pyqtgraph.org). I installed those dependancies. This didn't work. So, I purged the old version of GNURadio, added the most current, stable release (3.8) to my PPA, and installed. This fixed the issue with the Filter Design Tool.
* Naturally though, this did more bad than good. My RTL-SDR source block from [gr-osmosdr](https://osmocom.org/) didn't exist anymore, redering GNURadio to be useless (for my purpose). So, I did the calaculations I needed in the filter design and backtracked. I reversed all of the `apt-add-repository` commands I executed, removed all traces of GNURadio and its accesorries from my computer, updated everything, and reinstalled. Now, I again don't have filter design but do have a source block for my antenna.
