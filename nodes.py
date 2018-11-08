from notation import NOTES

class Node:
    def __init__(self,fret,string,branches):
        self.fret = fret
        self.string = string
        self.branches = branches

def idx2id(lst,i,j): # return specific consecutive ID of an index of a 2D array
    id2D = sum(len(x) for x in lst[0:i])
    id2D += len(lst[i][0:j])
    return id2D

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
                node.branches.append(idx2id(node_lst,i+1,j))
                j += 1
        i += 1

    return node_lst

def find_shortest_path(node_lst): # crap
    for level in node_lst:
        pass
    return 0