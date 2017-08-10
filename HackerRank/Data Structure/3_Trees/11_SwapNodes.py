N = int(raw_input().strip())

if N != 0:
    for i in range(N-1):
        arr = map(int,raw_input().strip().split(' '))
        if i == 0: # The first node -- root
            
            