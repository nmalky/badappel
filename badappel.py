import os
import pretty_midi

def playsound(freq, duration):
    os.system("play -q -n synth {} sin {}".format(duration, freq))
    
# https://pages.mtu.edu/~suits/notefreqs.html
notes = {
    'silence' : 0,
    'C4'  : 261.63,
    'C#4' : 277.18,
    'Db4' : 277.18,
    'D4'  : 293.66,
    'D#4' : 311.13,
    'Eb4' : 311.13,
    'E4'  : 329.63,
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



# https://onlinesequencer.net/1933089
def play():
    #playsound(notes['A4'], 0.1)
    #playsound(notes['B4'], 0.1)

    playsound(notes['D#5'], 0.2)

    playsound(notes['F5'], 0.2)
    playsound(notes['F#5'], 0.2)
    playsound(notes['G#5'], 0.2)
    playsound(notes['A#5'], 0.1)
    playsound(0, 0.2) # silence? 
    playsound(notes['A#5'], 0.1)
    playsound(notes['D#6'], 0.2)
    playsound(notes['C#6'], 0.2)
    playsound(notes['A#5'], 0.1)
    playsound(0, 0.2)
    playsound(notes['A#5'], 0.1)
    playsound(notes['D#5'], 0.1)
    playsound(0, 0.2)
    playsound(notes['D#5'], 0.1)
    playsound(notes['A#5'], 0.2)
    playsound(notes['G#5'], 0.2)
    playsound(notes['F#5'], 0.2)
    playsound(notes['F5'] , 0.2)
    playsound(notes['D#5'], 0.2)
    playsound(notes['F5'] , 0.2)
    playsound(notes['F#5'], 0.2)
    playsound(notes['G#5'], 0.2)
    playsound(notes['A#5'], 0.1)

# convert the midi note numbers (pitch) to lettered notes
pitch_to_notes = { 60 : 'C4',
                   61 : 'C#4', 
                   62 : 'D4',
                   63 : 'D#4', 
                   64 : 'E4', 
                   65 : 'F4', 
                   66 : 'F#4', 
                   67 : 'G4', 
                   68 : 'G#4',
                   69 : 'A4',
                   70 : 'A#4',
                   71 : 'B4' }

# generate higher and lower notes
for pitch in set(pitch_to_notes.keys()):
    note = pitch_to_notes[pitch]
    # replace 4 with 5, adding 12 to the pitch
    new_pitch = pitch + 12
    new_note =  note.replace('4','5')
    pitch_to_notes[new_pitch] = new_note

    # replace 4 with 6, adding 12 to the pitch
    new_pitch = pitch + 12*2
    new_note =  note.replace('4','6')
    pitch_to_notes[new_pitch] = new_note

    # replace 4 with 3, subtracting 12 from the pitch
    new_pitch = pitch + 12*-1
    new_note =  note.replace('4','3')
    pitch_to_notes[new_pitch] = new_note



def play_midi():
    # midi reading
    # https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S2_MIDI.html
    midi_data = pretty_midi.PrettyMIDI('./1933089_1.mid')
    midi_list = []

    for instrument in midi_data.instruments:
        for note in  instrument.notes:
            start = note.start
            end = note.end
            pitch = note.pitch
            velocity = note.velocity
            midi_list.append([start, end, pitch, velocity, instrument.name])

    midi_list = sorted(midi_list, key=lambda x: (x[0]))

    # play only the upper notes (melody)
    midi_list = list(filter(lambda x: x[2] >= 72-12, midi_list)) # C5
    # maybe our midi doesn't conform to the spec? (there aren't enough pitches >=72, but the sequencer shows the melody all above C5)

    # just play in order for the duration
    #for (start, end, pitch, velocity, instrument) in midi_list:
    #    duration = end-start
    #    note = pitch_to_notes[pitch]
    #    playsound(notes[note], duration)

    # account for pauses, and aggregate duplicate notes
    # compare each note with the next. disregard velocity and instrument
    processed_notes = []   # format: (note, duration)

    # just sequentially process by checking the difference between notes
    i = 0
    while i < len(midi_list):
        start1, end1, pitch1, velocity1, instrument1 = midi_list[i]

        # look ahead, process duplicates
        if i+1 < len(midi_list):
            start2, end2, pitch2, velocity2, instrument2 = midi_list[i+1]
            if end1 == start2 and pitch1 == pitch2:
                processed_notes.append((pitch_to_notes[pitch1], end2-start1))
                i = i + 2
                continue

        # add this note
        processed_notes.append((pitch_to_notes[pitch1], end1-start1))

        # detect silence between notes
        if i+1 < len(midi_list):
            start2, end2, pitch2, velocity2, instrument2 = midi_list[i+1]
            if start2 > end1:
                processed_notes.append(('silence', start2-end1))

        # move onto the next note
        i = i + 1

        



    for (note, duration) in processed_notes:
        playsound(notes[note], duration)




if __name__ == '__main__':
    #play();
    play_midi()

# step 1. populate note table
# step 2. get notes of bad apple
