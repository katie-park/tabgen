from notation import *
from random import randint

def melody_gen(n,instrument): # generates melody with n notes
	melody = []
	min_pitch = NOTES.index(instrument.tunings[0])
	max_pitch = NOTES.index(instrument.tunings[len(instrument.tunings)-1])+instrument.fretnum
	pitch_idx = randint(min_pitch,max_pitch)
	limit = 12
	for i in range(n):
		melody.append(NOTES[pitch_idx])
		pitch_idx = randint(pitch_idx-limit,pitch_idx+limit+1)
		while (pitch_idx < min_pitch) or (pitch_idx > max_pitch):
			pitch_idx = randint(pitch_idx-limit,pitch_idx+limit)
	return melody