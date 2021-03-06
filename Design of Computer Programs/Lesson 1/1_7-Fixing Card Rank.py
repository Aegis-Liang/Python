# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    dict_card = dict([('23456789TJQKA'[i-2], i) for i in range(15) if i > 1])
    ranks = [dict_card[r] for r,s in cards] 
    # Norvig's solution: ranks = ['--23456789TJQKA'.index(r) for r,s in cards] 
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]