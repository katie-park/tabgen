from display import *
from notation import *
from randnote import *
import sys

class Node:
    def __init__(self,fret,string,branches):
        self.fret = fret
        self.string = string

def gen_nodes(melody,instrument): # generate possible tab
    node_lst = []
    for pitch in melody:
        fret_choices = []
        for string in instrument.tunings:
            fret = NOTES.index(pitch) - NOTES.index(string)
            if fret >= 0 and fret <= instrument.fretnum: # check if pitch is in range of instrument's string
                fret_choices.append(Node(fret, string, []))
        node_lst.append(fret_choices)
    return node_lst

def stat_range(lst):
    return max(lst) - min(lst)

def path_length(tab, limit=None): # incorporate limits
    path_length = 0
    
    zero_start = False
    if tab[0].fret == 0:
        zero_start = True
    i = 1
    for node in tab[1:len(tab)]:
        if zero_start:
            if node.fret != 0:
                first_fret = node.fret
                zero_start = False
            i += 1
            continue

        if node.fret != 0:
            if tab[i-1].fret != 0:
                first_fret = tab[i-1].fret
                second_fret = node.fret
            else:
                second_fret = node.fret

            if type(limit) == int:
                if abs(first_fret - second_fret) > limit:
                    return None
            path_length += abs(first_fret - second_fret)

        else:
            if tab[i-1].fret != 0:
                first_fret = tab[i-1].fret
        i += 1
    return path_length

def tree_iterate(lst, limit=None):
    max_indices = [len(i)-1 for i in lst]
    
    ids = [0]*len(lst)

    done = False
    
    iterations = []
    j = 0

    shortest_iteration = None

    while not done:
        
        current_iteration = []

        for i in range(len(lst)):
            current_iteration.append(lst[i][ids[i]])
        
        if path_length(current_iteration,limit) != None:
             shortest_iteration = current_iteration

        # If limit
        elif type(limit) == int:
            if path_length(current_iteration,limit) != None:
                if path_length(current_iteration,limit) < path_length(shortest_iteration,limit):
                    shortest_iteration = current_iteration
                elif path_length(current_iteration,limit) == path_length(shortest_iteration,limit):
                    if stat_range([i.fret for i in current_iteration]) < stat_range([i.fret for i in current_iteration]):
                        shortest_iteration = current_iteration
                    if stat_range([i.fret for i in current_iteration]) == stat_range([i.fret for i in current_iteration]):
                        if sum([i.fret for i in current_iteration]) <= sum([i.fret for i in current_iteration]):
                            shortest_iteration = current_iteration

        # If no limit
        else:
            if path_length(current_iteration) < path_length(shortest_iteration):
                shortest_iteration = current_iteration
            elif path_length(current_iteration) == path_length(shortest_iteration):
                if stat_range([i.fret for i in current_iteration]) < stat_range([i.fret for i in current_iteration]):
                    shortest_iteration = current_iteration
                if stat_range([i.fret for i in current_iteration]) == stat_range([i.fret for i in current_iteration]):
                    if sum([i.fret for i in current_iteration]) <= sum([i.fret for i in current_iteration]):
                        shortest_iteration = current_iteration

        # Increment indices
        ids[len(ids)-1] += 1

        carry = False
        for i in range(len(ids)-1,-1,-1):
            if carry:
                ids[i] += 1
                carry = 0

            if i == 0 and ids[i] > max_indices[i]:
                done = True

            if ids[i] > max_indices[i]:
                carry = True
                ids[i] = 0

        iterations.append(path_length(current_iteration))

        j += 1

    return shortest_iteration

