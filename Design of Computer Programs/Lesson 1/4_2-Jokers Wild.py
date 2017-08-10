# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools
'''
# Norvig's solution
allranks = '23456789TJQKA'
redcards  = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)

def replacements(card):
    """Return a list of the possible replacements for a card.
    There will be more than 1 only for wild cards."""
    if card == "?B": return blackcards
    elif card == "?R": return redcards
    else: return [card]
'''

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    
    # Your code here
    # Categories the cards
    wild_cards = [x for x in hand if x[0] == "?"]     
    not_wild_cards = [x for x in hand if x[0] != "?"]
          
          
    # Generate a list for product use. 
    # Exp. ['2H', '2D', '3H', '3D', '4H', '4D', '5H', '5D', '6H', '6D', '7H', '7D', '8H', '8D', '9H', '9D', 'TH', 'TD', 'JH', 'JD', 'QH', 'QD', 'KH', 'KD', 'AH', 'AD']  
    red_cards = [x+y for x,y in itertools.product('23456789TJQKA', 'HD')]
    black_cards = [x+y for x,y in itertools.product('23456789TJQKA', 'SC')]
 
    # Unpack all the wild cards one by one into a list
    # Exp. [['2S', '2C', '3S', '3C', '4S', '4C', '5S', '5C', '6S', '6C', '7S', '7C', '8S', '8C', '9S', '9C', 'TS', 'TC', 'JS', 'JC', 'QS', 'QC', 'KS', 'KC', 'AS', 'AC']]
    wild_cards_actual = []
    for wc in wild_cards:
        if wc == '?R':
            wild_cards_actual.append(red_cards)    
        else:
            wild_cards_actual.append(black_cards)  
        
    # Generate all the wild cards possible permutation
    # When the we have only one wild card, we need a different way to generate the pattern (x,) 
    # which could be used for list(('2A',)) = ['2A'] not list('2A') = ['2','A']
    wild_cards_product = []      
    if len(wild_cards_actual)==1:
        wild_cards_product = [(x,) for x in reduce(itertools.product, wild_cards_actual)]
    elif len(wild_cards_actual) > 1:
        wild_cards_product = [x for x in reduce(itertools.product, wild_cards_actual)]
    else:
        wild_cards_product = []   


    # Concatenate the wild cards and not wild cards to generate the hand
    all_cards_hand = [] 
    if wild_cards_product == []:
        all_cards_hand = [tuple(not_wild_cards)]
    else:
        all_cards_hand = [tuple(list(x)  + not_wild_cards) for x in wild_cards_product]

    # Return the max hand
    return max([max(itertools.combinations(x, 5), key=hand_rank) for x in all_cards_hand], key=hand_rank)


    
    

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
    
if __name__ == "__main__":
    test_best_wild_hand();

