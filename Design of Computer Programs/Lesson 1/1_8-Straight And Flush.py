# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return reduce(lambda x, y : x and y, [ranks[i]==ranks[i+1]+1 for i in range(len(ranks)-1)])
    # Norvig's solution:
    # return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return reduce(lambda x, y : x and y, [suits[i]==suits[i+1] for i in range(len(suits)-1)])
    # Norvig's solution:
    # return len(set(suits)) == 1
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

print test()