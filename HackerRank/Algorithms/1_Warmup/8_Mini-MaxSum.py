#arr = map(int, raw_input().strip().split(' '))

arr = [1, 2, 3, 4, 5]
print str(sum(arr) - max(arr)) + " " + str(sum(arr) - min(arr))