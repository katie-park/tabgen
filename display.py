from math import trunc
from random import randint, choice
from nodes import Node, genNodes

def dispNodes(lst, melody, branches = False):
    table = ""
    for level, pitch in zip(lst, melody):
        table += pitch + ": "
        for node in level:
            table += str(node.fret) + '(' + node.string + ") "
            if branches == True:
                table += str(node.branches) + "\n" + (len(pitch)+2)*' '
        table += "\n"
    return table


def dispTab(tab,instrument): # displays ASCII tablature # outdated
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
    return lines

    
