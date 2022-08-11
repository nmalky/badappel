import os

def playsound(freq, duration):
    os.system("play -q -n synth {} sin {}".format(duration, freq))
    
# https://pages.mtu.edu/~suits/notefreqs.html
notes = {
    'C4'  : 261.63,
    'C#4' : 277.18,
    'Db4' : 277.18,
    'D4'  : 293.66,
    'D#4' : 311.13,
    'Eb4' : 311.13,
    'F4'  : 349.23,
    'Gb4' : 369.99,
    'F#4' : 369.99,
    'G4'  : 392.00,
    'G#4' : 415.30,
    'Ab4' : 415.30,
    'A4'  : 440,
    'A#4' : 466.16, 
    'Bb4' : 466.16, 
    'B4'  : 493.88,
    }

for note in set(notes.keys()): # prevent changing size during iteration
    # substitute the 4 for a 5, and double the frequency
    new_note = note.replace('4','5')
    new_freq = notes[note] * 2
    notes[new_note] = new_freq

    # do the same for 6 i guess
    new_note = note.replace('4','6')
    new_freq = notes[note] * 4
    notes[new_note] = new_freq

# we could double and halve these successively 
# but it may just be easier to copy/paste




def play():
    #playsound(notes['A4'], 0.1)
    #playsound(notes['B4'], 0.1)

    playsound(notes['D#5'], 0.2)

    playsound(notes['F5'], 0.2)
    playsound(notes['F#5'], 0.2)
    playsound(notes['G#5'], 0.2)


if __name__ == '__main__':
    play();

# step 1. populate note table
# step 2. get notes of bad apple
