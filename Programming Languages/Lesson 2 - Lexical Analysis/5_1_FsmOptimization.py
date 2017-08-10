# Title: FSM Optimization
# 
# Challenge Problem: 2 Stars
#
# Lexical analyzers are implemented using finite state machines generated
# from the regular expressions of token definition rules. The performance
# of a lexical analyzer can depend on the size of the resulting finite
# state machine. If the finite state machine will be used over and over
# again (e.g., to analyze every token on every web page you visit!), we
# would like it to be as small as possible (e.g., so that your webpages
# load quickly). However, correctness is more important than speed: even
# an optimized FSM must always produce the right answer.  
#
# One way to improve the performance of a finite state machine is to make
# it smaller by removing unreachable states. If such states are removed,
# the resulting FSM takes up less memory, which may make it load faster or
# fit better in a storage-constrained mobile device.
#
# For this assignment, you will write a procedure nfsmtrim that removes
# "dead" states from a non-deterministic finite state machine. A state is
# (transitively) "dead" if it is non-accepting and only non-accepting
# states are reachable from it. Such states are also called "trap" states:
# once entered, there is no escape. In this example FSM for r"a*" ...
#
# edges = { (1,'a') : [1] ,
#           (1,'b') : [2] ,
#           (2,'b') : [3] ,
#           (3,'b') : [4] } 
# accepting = [ 1 ] 
# 
# ... states 2, 3 and 4 are "dead": although you can transition from 1->2,
# 2->3 and 3->4 on "b", you are doomed to rejection if you do so. 
#
# You may assume that the starting state is always state 1. Your procedure
# nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting)
# corresponding to a FSM that accepts exactly the same strings as the input
# FSM but that has all dead states removed. 
#
# Hint 1: This problem is tricky. Do not get discouraged. 
#
# Hint 2: Think back to the nfsmaccepts() procedure from the "Reading
# Machine Minds" homework problem in Unit 1. You are welcome to reuse your
# code (or the solution we went over) to that problem. 
#
# Hint 3: Gather up all of the states in the input machine. Filter down
# to just those states that are "live". new_edges will then be just like
# edges, but including only those transitions that involve live states.
# new_accepting will be just like accepting, but including only those live
# states. 

#from sets import Set

def nfsmaccepts(current, edges, accepting, visited):
    if current in visited:
        return None
    elif current in accepting:
        return ""
    else:
        newvisited = visited + [current]
        for edge in edges:
            if edge[0] == current:
                for newstate in edges[edge]:
                    foo = nfsmaccepts(newstate, edges, accepting, newvisited)
                    if foo != None:
                        return edge[1] + foo
        return None    
    #if current in visited:
        #return None, {}
    #elif current in accepting:
        #return "", {}
    #else:
        #newvisited = visited + [current]
        #for edge in edges:
            #if edge[0] == current:
                #for newstate in edges[edge]:
                    ## update recorded_edges
                    #foo, recorded_edges = nfsmaccepts(newstate, edges, accepting, newvisited)
                    #if foo != None:
                        #if edge in recorded_edges:
                            #recorded_edges[edge].append(newstate)
                        #else:
                            #recorded_edges[edge] = [newstate]
                        #return edge[1] + foo, recorded_edges
        #return None, {}
    
#def trim_edges(current, edges, accepting, walked_edges):
    #new_edges = {}
    #new_accepting = []    

    #for edge in edges:
        #if edge[0] == current:
            #for newstate in edges[edge]:
                
                
                ##if newstate not in walked_edges.get(edge,[]):  
                #if could_continue(newstate, edges, walked_edges):
                    #if edge not in walked_edges:
                        #walked_edges[edge] = [newstate]                      
                    #else: 
                        #if newstate not in walked_edges[edge]:
                            #walked_edges[edge].append(newstate)        
                    ## This one is wrong
                    ## walked_edges[edge] = walked_edges.get(edge,[]).append(newstate)
                    ## [].append(1) =========> None
                    ## x = [], x.append(1) x =========> [1]
                      
                    #edges[edge].remove(newstate)
                    ##walked_edges_temp = walked_edges.copy()
                    #result1, result2 = trim_edges(newstate, edges, accepting, walked_edges)  
                                                                                                          
                    #if newstate in accepting:
                        #new_edges = merge_dicts(merge_dicts(new_edges, result1), walked_edges) # use walked_edges_temp could solve a problem, but issue another problem
                        #new_accepting.extend(result2)
                        #new_accepting.append(newstate)   # make a condition could solve the issue that new_accepting is [1,1]
                    #else:
                        #new_edges = merge_dicts(new_edges, result1)
                        #new_accepting.extend(result2)

                #else:
                    #if edge not in walked_edges:
                        #walked_edges[edge] = [newstate]
                    #else: 
                        #if newstate not in walked_edges[edge]:
                            #walked_edges[edge].append(newstate)
                        
                    #if newstate in accepting:
                        #new_edges = merge_dicts(new_edges, walked_edges)
                        #new_accepting.append(newstate)
                    #else:
                        #pass
    #return new_edges, new_accepting
           
#def could_continue(newstate, edges, walked_edges):
    #for edge in edges:
        #if edge[0] == newstate:
            #if edge not in walked_edges:
                #return True
            #if newstate not in walked_edges[edge]:
                #return True
    #return False
                    
#def merge_dicts(dict1, dict2):

    #dict_all = {}
    #set_keys = Set([])
    
    
    #if dict1 == None:
        #dict1 = {}    
    #if dict2 == None:
        #dict2 = {}    
    
    #for key1 in dict1:
        #set_keys.add(key1)
    #for key2 in dict2:
        #set_keys.add(key2)
        
    #for key in set_keys:
        #dict_all[key] = []
        #if key in dict1:
            #for value in dict1[key]:
                #dict_all[key].append(value)
        #if key in dict2:
            #for value in dict2[key]:
                #if value not in dict_all[key]:
                    #dict_all[key].append(value)     
    #return dict_all
    

def nfsmtrim(edges, accepting): 
    ## Write your code here.
    # Gather up all of the states, possibly with duplicates.
    states = []
    for e in edges:
        states = states + [e[0]] + edges[e]
    
    # A state is live if there is some way to accept starting from it.
    live = []
    for s in states:
        if nfsmaccepts(s, edges, accepting, []) != None:
            live = live + [s]
    
    # Now that we know what is live, build up the output.
    new_edges = {}
    for e in edges:
        if e[0] in live:
            new_destinations = []
            for destincation in edges[e]:
                if destincation in live:
                    new_destinations = new_destinations + [destincation]
            if new_destinations != []:
                new_edges[e] = new_destinations
    new_accepting = []
    for s in accepting:
        if s in live:
            new_accepting = new_accepting + [s]
    return (new_edges, new_accepting)
    #return trim_edges(1, edges, accepting, {})
    
    #new_edges = {}
    #new_accepting = []
    
    #for accept in accepting:
        #accept_string, accept_dict = nfsmaccepts(1, edges, accepting, [])
        #if accept_string != None:
            #for item in accept_dict:
                #if item in new_edges:
                    #if accept_dict[item] not in new_edges[item] and accept_dict[item] != new_edges[item]:
                        #new_edges[item].extend(accept_dict[item])
                #else:
                    #new_edges[item] = accept_dict[item]
            #new_accepting.append(accept)
        #else:
            #pass
    #return new_edges, new_accepting
                

        
#edgesx = { (1, 'a') : [2, 3],
          #(2, 'a') : [2],
          #(3, 'b') : [4, 2],
          #(4, 'c') : [5]}
#acceptingx = [5]      
#print nfsmaccepts(1, edgesx, acceptingx, [])

        


# We have included a few test cases, but you will definitely want to make
# your own. 

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , } 
accepting1 = [ 1 ] 

#print trim_edges(1, edges1, accepting1, {})


(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 
print "1:"
print new_edges1
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1] 

print "2:"
(new_edges2, new_accepting2) = nfsmtrim(edges1,[]) 
print new_edges2 == {}
print new_accepting2 == [] 

print "3:"
print nfsmaccepts(1, edges1, [3, 6], [])
print ''
(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6]) 
print new_edges3
print new_accepting3
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]

print "4:"
edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
accepting4 = [ 2 ] 
(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4) 
print new_edges4
print new_accepting4
print new_edges4 == { 
  (1, 'a'): [1],
  (1, 'b'): [2], 
  (2, 'b'): [3], 
  (3, 'c'): [2, 1], 
}
print new_accepting4 == [2]
