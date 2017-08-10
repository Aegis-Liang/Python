# Tricky REs with ^ and \

# Assign to regexp a regular expression for double-quoted string literals that
# allows for escaped double quotes.

# Hint: Escape " and \
# Hint: (?: (?: ) )

import re

#regexp = r'\"(?:\\\\|\\\"|[^\\])*\"' # Acutally I have no idea how this could pass the tests
regexp = r'"(?:[^\\]|(?:\\.)*)*"' # Answer

# regexp matches:
print re.findall(regexp,'"I say, \\"hello.\\""')
print '"I say, \\"hello.\\""'
print re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']
#>>> True


# regexp does not match:

print re.findall(regexp,'"\\"')
print '"\\"'
print re.findall(regexp,'"\\"') != ['"\\"']
#>>> True

