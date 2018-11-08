octave = 0
NOTES = [] # array of 88 notes, scientific pitch notation
for n in range(9): # fill notes
    i = 0
    for n in range(12):
        note = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"][i]
        note += str(octave)
        NOTES.append(note)
        i += 1
        if note == "C8":
            break
    octave += 1

class Instrument:
    def __init__(self,tunings,fretnum):
        self.tunings = tunings
        self.fretnum = fretnum

guitar = Instrument(['E2','A2','D3','G3','B3','E4'],19)
bass_guitar = Instrument(['E2','A2','D3','G3'],20)

INSTRUMENTS = (guitar,bass_guitar)

def enharmonic(pitch): # unfinished
    white_keys = ['C','D','E','F','G','A','B']
    if pitch[0] == any(white_keys):
        if pitch[1] == 'b':
            enharmonic_pitch = white_keys[white_keys.index(pitch[0])-1] + "#"
    return 0