"""
6 different color permutation: 6! = 720
3 black and 3 white permutation: 6!/(3!*3!)=20

k objects repeat: n!/k!
j objects repeat and k object repeat: n!/(j!k!)


20 Horses, guess which 3 will get first 3 in order.
P: n!/(n-r)! = 20!/(20-3)! = 6840

20 Horses, guess which 3 will get first 3, order is not matter.
C: n!/((n-r)!r!) = 20!/((20-3)!3!) = 1140
"""
import itertools

if __name__ == "__main__":
    print len(list(itertools.permutations([x for x in range(20)],3)))
    print len(list(itertools.combinations([x for x in range(20)],3)))