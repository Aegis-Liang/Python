for x in items:
    print x
    
# ===================>>>

i = 0
while i < len(items):
    x = items[i]
    print x
    

# Itemable
it = iter(items)
try:
    while True:
        x = next(it)
        print x
except StopIteration:
    pass