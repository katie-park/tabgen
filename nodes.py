from notation import NOTES

def difference(pitch,string):
    if pitch >= string:
        return pitch - string
    else:
        return None

class Node:
    def __init__(self,fret,string,branches):
        self.fret = fret
        self.string = string
        self.branches = branches

def genNodes(melody,instrument): # generate possible tab
    node_lst = []
    for pitch in melody:
        fret_choices = []
        for string in instrument.tunings:
            if NOTES.index(pitch) >= NOTES.index(string):
                fret_choices.append(Node(difference(NOTES.index(pitch), NOTES.index(string)), string, []))
        node_lst.append(fret_choices)

    return node_lst