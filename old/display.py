from math import trunc
from random import randint, choice
import sys

def dispNodes(lst,melody):
    node_display = ""
    for level, pitch in zip(lst, melody):
        node_display += pitch + ": "
        for node in level[0:len(level)-1]:
            node_display += str(node.fret) + '(' + node.string + ")"
            node_display += ", "
        node_display += str(level[len(level)-1].fret) + '(' + level[len(level)-1].string + ")"
        node_display += "\n"
    return node_display

def dispTab(tab,instrument): # displays ASCII tablature
    lines = []
    for i in instrument.tunings:
        lines.append(i[0]+"|")
    i = 0
    for node in tab:
        j = 0
        for x in lines:
            dashnum = len(str(node.fret)) + 1
            if j == instrument.tunings.index(node.string):
                #to do: fill it bitch
                lines[j] += str(node.fret)
                lines[j] += "-"
            else:
                lines[j] += "-" * dashnum
            j += 1
        i += 1
    lines.reverse()

    return "\n".join(lines)
    
