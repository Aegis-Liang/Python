# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

# My solution: (Cannot work by their tests and don't know why)
'''def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    hands = []*numhands
    random.shuffle(mydeck)
    for h in range(numhands):
        cards = []*n
        for c in range(n):
            cards.append(mydeck.pop())
        hands.append(cards)
    return hands
'''

# Norvig's solution:
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]


if(__name__=="__main__"):
    hands = deal(2, 7)
    print(hands)