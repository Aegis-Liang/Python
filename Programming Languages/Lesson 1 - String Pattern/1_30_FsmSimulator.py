# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # QUIZ: You fill this out!
        # Is there a valid edge?
        if (current, letter) in  edges:
        # If so, take it.
            current = edges[(current, letter)]
            return fsmsim(string[1:], current, edges, accepting)
        # If not, return False.
        else:
            return False
            #return current in accepting # This could make fsmsim("a12",1,edges,accepting) True which should be False
        # Hint: recursion.


print fsmsim("aaa111",1,edges,accepting)
# >>> True
print fsmsim("a1",1,edges,accepting)
print fsmsim("a12",1,edges,accepting)