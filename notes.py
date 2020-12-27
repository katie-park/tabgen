import re # is it worth it to import regex for only one line of code? 🤷🏻‍♀️
from fractions import Fraction
from math import ceil

# Abstraction of musical pitch and length of time
class Pitch:
    scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    scale_len = len(scale) # 12 (number of notes in a scale)

    def __init__(self, number: int):
        self.number = number
        self.octave = int(number / scale_len) # rounding down by typecasting to int
        self.pitch_class = number % scale_len # do i need pitch class as a public attribute?
        self.name = scale[self.pitch_class] + str(octave)
        
    @classmethod # this method is kinda lame since i'm calculating octave and pitch class twice... maybe find a better alternative later?
    def fromName(cls, name: str):
        octave = int(re.search(r"\d+$", name).group()) # https://stackoverflow.com/questions/7085512/check-what-number-a-string-ends-with-in-python
        pitch_class = scale.index(name[0]) # https://en.wikipedia.org/wiki/Pitch_class
        number = pitch_class + (12 * octave) + name.count('#') - name.count('b') # '#' represents sharps, 'b' represents flats
        return cls(number)

    def __str__(self):
        return self.name + ", " + str(self.number)
    def __int__(self):
        return self.number

class Length:
    def __init__(self, num_of_beats: Fraction, beat_unit: int):
        self.num_of_beats = num_of_beats # the number of beats (based on the beat_unit) that the length lasts
        self.beat_unit = beat_unit # the note value of one beat, typically a power of 2
    
    def __int__(self): # measured by quarter notes
        quarter_note = 4 # enum?
        return num_of_beats * Fraction(quarter_note, beat_unit)


# Abstraction of instruments
class String: # The string of an instrument (not an array of characters! maybe this name is confusing but i can't think of an alternative yet)
    def __init__(self, tuning, num_of_frets):
        self.tuning = tuning
        self.num_of_frets = num_of_frets
    
    def fret(self, num): # returns the pitch at a specified pitch number
        if not (0 <= num and num <= num_of_frets):
            raise ValueError("num must be a noneegative integer less than or equal to the num_of_frets of the String")
        

class Instrument: # In the scope of this program, only stringed instruments are used.
    def __init__(self, tunings: [Pitch]):
        self.tunings = tunings


# Abstraction of songs
class Note:
    def __init__(self, pitch: Pitch, length: Length, start_time):
        self.pitch = pitch
        self.length = length
        self.start_time = start_time # when the note starts, based on int(length). see Song for more context. (maybe type restrict to Fraction?)

class Song:
    def __init__(self, time_signature: Length, notes: [Note]): # uhhhh
        self.time_signature = time_signature
        self.notes = notes # notes in the song. start_time dictates when in the song a note occures
        self.num_of_measures = ceil(max(notes, key=lambda x: x.start_time) / time_signature.length) # number of measures in the song
    
    def uhhh(self, instrument: Instrument):
        pass