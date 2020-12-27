from fractions import Fraction
from math import ceil
from sound_properties import *
from instrument import *


# Abstraction of tablature
class Note:
    def __init__(self, pitch: Pitch, length: Length, start_time: Fraction):
        self.pitch = pitch
        self.length = length
        self.start_time = start_time # when the note starts, based on int(length). see Song for more context.
    
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