class Instrument:
    def __init__(self,name,tunings,fretnum):
        self.name = name
        self.tunings = tunings
        self.fretnum = fretnum

guitar = Instrument("guitar",['E2','A2','D3','G3','B3','E4'],19)
bass_guitar = Instrument("bass guitar",['E2','A2','D3','G3'],20)
ukulele = Instrument("ukulele",['G3','C4','E4','A4'],12)

INSTRUMENTS = (guitar,bass_guitar,ukulele)

# Notes
Cchromatic =["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
NOTES = []
for octave in range(8):
    for pitch_class in range(12):
        pitch = Cchromatic[pitch_class]
        pitch += str(octave)
        NOTES.append(pitch)
NOTES.append(Cchromatic[0]+str(8)) # append pitch C8

def similar_str(test_str,original_str):
    if test_str[0:len(original_str)] == original_str:
        return True
    else:
        return False

def enharmonic(pitch): # unfinished
    global NOTES
    if pitch in NOTES: return pitch
    elif pitch[0:3] == "C##": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:3] == "D##": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:3] == "E#": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:3] == "F##": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:3] == "G##": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:3] == "A##": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]
    elif pitch[0:2] == "B#": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])+1]

    elif pitch[0:3] == "Cbb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Dbb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Ebb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Fbb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Gbb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Abb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]
    elif pitch[0:3] == "Bbb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-2]

    elif pitch[0:2] == "Cb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Db": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Eb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Fb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Gb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Ab": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    elif pitch[0:2] == "Bb": return NOTES[NOTES.index(pitch[0]+pitch[len(pitch)-1])-1]
    else: return None


