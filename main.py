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

if method == 2:

	chosen_instrument = choice(notation.INSTRUMENTS)
	min_pitch = notation.NOTES.index(chosen_instrument.tunings[0])
	max_pitch = notation.NOTES.index(chosen_instrument.tunings[len(chosen_instrument.tunings)-1])+chosen_instrument.fretnum

	melody = []
	for i in range(randint(2,5)):
		melody.append(choice(notation.NOTES[min_pitch:max_pitch]))

	print(display.dispNodes(nodes.genNodes(melody,chosen_instrument), melody))
	
