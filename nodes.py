from notation import NOTES
from random import choice

class Node:
    def __init__(self,fret,string,branches):
        self.fret = fret
        self.string = string
        self.branches = branches

def idx2id(lst,i,j): # return specific ID from an index of a 2D array
    id2D = sum(len(x) for x in lst[0:i])
    id2D += len(lst[i][0:j])
    return id2D

def id2idx(lst,id2D): # return index of a 2D array from a specific ID # crap
    n = 0
    i = 0
    j = 0
    #uhhhh
    return i, j

'''
test = [[0,1,2],[3],[4,5]]
i = 0
n = 0
for x in test:
    j = 0
    for y in x:
        print(idx2id(test,i,j),id2idx(test,n))
        j += 1
        n += 1
    i += 1
'''

def genNodes(melody,instrument): # generate possible tab
    node_lst = []
    for pitch in melody:
        fret_choices = []
        for string in instrument.tunings:
            if NOTES.index(pitch) >= NOTES.index(string):
                fret_choices.append(Node(NOTES.index(pitch)-NOTES.index(string), string, []))
        node_lst.append(fret_choices)

    # generate branches
    i = 0
    for level in node_lst[0:len(node_lst)-1]:
        for node in level:
            j = 0
            for branch in node_lst[i+1]:
                if node.fret == 0 and branch.fret == 0:
                    node.branches.append("BN")
                elif node.fret == 0:
                    node.branches.append("B"+str(branch.fret))
                elif branch.fret == 0:
                    node.branches.append("N"+str(node.fret))
                else:
                    node.branches.append(abs(node.fret-branch.fret))
                j += 1
        i += 1

    return node_lst

def link(level):
    for level in lst:
        for node in lst:
            pass
    return 0

def rand_path(node_lst):
    tab = []
    for level in node_lst:
        tab.append(choice(level))
    return tab


def find_shortest_path(node_lst,instrument): # crap
    limit = instrument.fretnum
    i = 0
    for level in node_lst[0:len(node_lst)-1]:
        j = 0
        for node in level:
            k = 0
            for difference in node.branches:
                for branch in node_lst[i+1][k]:
                    branch.branches 
                k += 1
            j += 1
        i += 1
    return 0