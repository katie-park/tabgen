import re
from fractions import Fraction

# Abstraction of musical pitch and length of time
class Pitch:
    scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    scale_len = len(scale) # 12 (number of notes in a scale)

    def __init__(self, number: int):
        self.number = number
        self.octave = int(number / Pitch.scale_len) # rounding down by typecasting to int
        self.pitch_class = number % Pitch.scale_len # do i need pitch class as a public attribute?
        self.name = Pitch.scale[self.pitch_class] + str(self.octave)
        
    @classmethod # this method is kinda lame since i'm calculating octave and pitch class twice... maybe find a better alternative later?
    def fromName(cls, name: str):
        octave = int(re.search(r"\d+$", name).group()) # https://stackoverflow.com/questions/7085512/check-what-number-a-string-ends-with-in-python
        pitch_class = scale.index(name[0]) # https://en.wikipedia.org/wiki/Pitch_class
        number = pitch_class + (scale_len * octave) + name.count('#') - name.count('b') # '#' represents sharps, 'b' represents flats
        return cls(number)

    def __str__(self):
        return self.name + ", pitch number: " + str(self.number)
    def __int__(self):
        return self.number

class Length:
    def __init__(self, num_of_beats: Fraction, beat_unit: int):
        self.num_of_beats = num_of_beats # the number of beats (based on the beat_unit) that the length lasts
        self.beat_unit = beat_unit # the note value of one beat, typically a power of 2
    
    def __int__(self): # measured by quarter notes
        quarter_note = 4 # enum?
        return num_of_beats * Fraction(quarter_note, beat_unit)