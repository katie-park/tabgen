from display import *
from nodes import *
from notation import *
from randnote import *

import sys
from random import randint, choice

print()
print(r"  _        _                                 _           ")
print(r" | |_ __ _| |__   __ _ ___ _ _  ___ _ _ __ _| |_ ___ _ _ ")
print(r" |  _/ _` | '_ \ / _` / -_| ' \/ -_| '_/ _` |  _/ _ | '_|")
print(r"  \__\__,_|_.__/ \__, \___|_||_\___|_| \__,_|\__\___|_|  ")
print(r"                 |___/                                   ")
print()

# randomized mode
if "-r" in sys.argv:
	chosen_instrument = ukulele
	melody = melody_gen(randint(2,20),chosen_instrument)

elif "-e" in sys.argv:
	chosen_instrument = ukulele
	melody = ["C5","B4","A4","G4","F4","G4","A4","C5","B4","A4","G4","F4","E4"]

# manual mode
else:
	print("INSTRUMENTS: ")
	i = 1
	for instrument in INSTRUMENTS:
		print(f"{i}. {instrument.name}")
		i += 1
	try:
		chosen_instrument = INSTRUMENTS[int(input(f"Select Instrument (1-{len(INSTRUMENTS)}): "))-1]
	except ValueError:
		print("error: instrument selection is not a number")
		sys.exit()
	except IndexError:
		print("error: instrument selection is out of range")
		sys.exit()
	melody = input("Input in scientific pitch (e.g. E3 G#3 Db3 ... ): ").split()
	melody = [enharmonic(i) for i in melody]

node_lst = gen_nodes(melody,chosen_instrument)
try:
	tab = tree_iterate(node_lst, 5)
	if tab == None:
		print("error: limit too high")
		sys.exit()
except IndexError:
	print("error: melody out of range")
	sys.exit()

if "-t" in sys.argv:
	print("MELODY: " + " ".join(melody))


print(chosen_instrument.name.upper())
print(dispTab(tab,chosen_instrument))

print("path length: " + str(path_length(tab)))
	
