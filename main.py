from random import randint, choice
import display
import nodes
import notation

print("TAB GENERATOR")
print("Manual input (1)")
print("Random input (2)\n")

try:
	method = int(input("Method: (1-2): "))
	print()
except ValueError:
	print("Stoopid")

if method == 1:
	melody = input("Input in scientific pitch notation (e.g. E3 A3 G3 ... ): ").split()

	chosen_instrument = notation.guitar

if method == 2:

	chosen_instrument = choice(notation.INSTRUMENTS)

	min_pitch = notation.NOTES.index(chosen_instrument.tunings[0])
	max_pitch = notation.NOTES.index(chosen_instrument.tunings[len(chosen_instrument.tunings)-1])+chosen_instrument.fretnum

	melody = []
	for i in range(randint(2,10)):
		melody.append(notation.NOTES[randint(min_pitch,max_pitch)])

print(display.dispNodes(nodes.genNodes(melody,chosen_instrument), melody, True))

for i in (display.dispTab(nodes.rand_path(nodes.genNodes(melody,chosen_instrument)),chosen_instrument)):
	print(i)
	
