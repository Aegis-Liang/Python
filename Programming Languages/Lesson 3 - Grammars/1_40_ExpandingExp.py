# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):                    # tokens: ["a", "token"]
    for pos in range(len(tokens)):
        for rule in grammar:                    # rule: ("exp", ["exp", "+", "exp"]),
            ls = []
            if tokens[pos] == rule[0]:           
                ls.extend(rule[1])
            else:
                ls.append(tokens[pos])
            yield ls
            # Offical Answer:
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]
            
            
depth = 1
utterances = [["exp"]] # [["a", "exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)] # expand(["exp"], grammar) or expand(["a", "exp"], grammar)

for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']