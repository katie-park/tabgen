import re # is it worth it to import regex for only one line of code? 🤷🏻‍♀️
from fractions import Fraction
from math import ceil

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


# Abstraction of instruments
class String: # The string of an instrument (not an array of characters! this name might be confusing but i can't think of an alternative yet)
    id = 0

    def __init__(self, tuning: Pitch, num_of_frets: int):
        self.tuning = tuning
        self.num_of_frets = num_of_frets
        self.id = String.id
        String.id += 1
    
    def pitch(self, fret_num): # returns the pitch at a specified fret number
        if not (0 <= fret_num and fret_num <= num_of_frets):
            raise ValueError("num must be a noneegative integer less than or equal to the num_of_frets of the String")
        return Pitch(int(self.tuning) + fret_num)
    
    def fret(self, pitch):
        return int(pitch) - int(tuning) # does not check if fret is out of range, containsPitch() does that (maybe this is bad)
    
    def containsPitch(self, pitch: Pitch): # to-do: remove redundancy of fret calculations
        fret = fret(pitch)
        if 0 <= fret and fret <= self.num_of_frets:
            return fret # if true (maybe this is also very bad)
        return False
    
    def __str__(self):
        return str(self.tuning) + " id: " + str(self.id)
        
class Instrument: # In the scope of this program, only stringed instruments are used.
    def __init__(self, strings: [String]):
        self.strings = strings # ordered?

    def stringsThatContain(self, pitch: Pitch):
        return filter(lambda x: x != False, [s.containsPitch() for s in strings]) # gross


# Abstraction of tablature
class Note:
    def __init__(self, pitch: Pitch, length: Length, start_time):
        self.pitch = pitch
        self.length = length
        self.start_time = start_time # when the note starts, based on int(length). see Song for more context. (maybe type restrict to Fraction?)
    
    def interval(self, ending_note):
        return int(ending_note.pitch) - int(self.pitch)

class Song:
    def __init__(self, time_signature: Length, notes: [Note]): # uhhhh
        self.time_signature = time_signature
        self.notes = notes.sort(key=lambda x: x.start_time) # notes in the song. start_time dictates when in the song a note occurs. sort from smallest to largest start_time to get notes in playing order
        self.num_of_measures = ceil(max(notes, key=lambda x: x.start_time) / time_signature.length) # number of measures in the song

class TabGraph:
    def __init__(self, song: Song, instrument: Instrument):
        self.song = song
        self.instrument = instrument
        nodes = []
        for note in song.notes:
            
            nodes.append("Test")