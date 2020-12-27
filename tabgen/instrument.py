from sound_properties import *

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