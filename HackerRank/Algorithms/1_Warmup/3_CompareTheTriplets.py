def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = [a0, a1, a2]
    b = [b0, b1, b2]

    s1 = map(int.__cmp__, a, b).count(1)
    s2 = map(int.__cmp__, b, a).count(1)
    return (s1,s2)

#a0, a1, a2 = raw_input().strip().split(' ')
#a0, a1, a2 = [int(a0), int(a1), int(a2)]
#b0, b1, b2 = raw_input().strip().split(' ')
#b0, b1, b2 = [int(b0), int(b1), int(b2)]
a0, a1, a2 = [5, 6, 7]
b0, b1, b2 = [3, 6, 10]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


