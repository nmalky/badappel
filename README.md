# badappel
questionable implementation of music. intended for adaptation to robot beeps

Acquire `play` from `sox`

Musics from https://onlinesequencer.net/1933089

## run
`sudo apt install sox`

`pip install -r requirements.txt` (just installs pretty_midi) 

then

`python3 badappel.py`

## future improvements
* export the midi to a list of (frequency, duration) pairs. load and play later without the dependency on midi parsing
* make it run on a roboto power board
