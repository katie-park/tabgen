octave = 0
NOTES = [] # array of 88 notes, scientific pitch notation
for i in range(9): # fill notes
    index = 0
    for i in range(12):
        note = ""
        note += ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"][index]
        note += str(octave)
        NOTES.append(note)
        index += 1
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