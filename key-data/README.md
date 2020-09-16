# Vehicle Key Fob Data

## The Idea


## Challenges
**I needed a FIR filter; but, GNURadio's Filter Design Tool wouldn't work.**
* I went to GitHub and searched GNURadio's issues. Sure enough, someone else had an identical issue. I downloaded the source from their repo, then isolated the Design Tool's script. It's attempted execution returned dependancy issues with [PyQTGraph](www.pyqtgraph.org). I installed those dependancies. This didn't work. So, I purged the old version of GNURadio, added the most current, stable release (3.8) to my PPA, and installed. This fixed the issue with the Filter Design Tool.
* Naturally though, this did more bad than good. My RTL-SDR source block from [gr-osmosdr](https://osmocom.org/) didn't exist anymore, redering GNURadio to be useless (for my purpose). So, I did the calaculations I needed in the filter design and backtracked. I reversed all of the `apt-add-repository` commands I executed, removed all traces of GNURadio and its accesorries from my computer, updated everything, and reinstalled. Now, I again don't have filter design but do have a source block for my antenna.
