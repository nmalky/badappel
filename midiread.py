# midi reading
# https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S2_MIDI.html
import pretty_midi

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

for note in midi_list:
    print(note)
