""" Boolean
Operation Name            Operator    Explanation
less than                 <           Less than operator 
greater than              >           Greater than operator 
less than or equal        <=          Less than or equal to operator 
greater than or equal     >=          Greater than or equal to operator 
equal                     ==          Equality operator 
not equal                 !=          Not equal operator 
logical and               and         Both operands True for result to be True 
logical or                or          One or the other operand is True for the result to be True 
logical not               not         Negates the truth value, False becomes True, True becomes False 
"""


""" List
Operation Name            Operator    Explanation
indexing                  []          Access an element of a sequence 
concatenation             +           Combine sequences together 
repetition                *           Concatenate a repeated number of times 
membership                in          Ask whether an item is in a sequence 
length                    len         Ask the number of items in the sequence 
slicing                   [:]         Extract a part of a sequence 

Method Name               Use                    Explanation
append                    alist.append(item)     Adds a new item to the end of a list 
insert                    alist.insert(i,item)   Inserts an item at the ith position in a list 
pop                       alist.pop()            Removes and returns the last item in a list 
pop                       alist.pop(i)           Removes and returns the ith item in a list 
sort                      alist.sort()           Modifies a list to be sorted 
reverse                   alist.reverse()        Modifies a list to be in reverse order 
del                       del alist[i]           Deletes the item in the ith position 
index                     alist.index(item)      Returns the index of the first occurrence of item 
count                     alist.count(item)      Returns the number of occurrences of item 
remove                    alist.remove(item)     Removes the first occurrence of item 
"""


""" String
Method Name               Use                    Explanation
center                    astring.center(w)      Returns a string centered in a field of size w 
count                     astring.count(item)    Returns the number of occurrences of item in the string 
ljust                     astring.ljust(w)       Returns a string left-justified in a field of size w 
lower                     astring.lower()        Returns a string in all lowercase 
rjust                     astring.rjust(w)       Returns a string right-justified in a field of size w 
find                      astring.find(item)     Returns the index of the first occurrence of item 
split                     astring.split(schar)   Splits a string into substrings at schar 
"""


""" Set
Operation Name            Operator               Explanation
membership                in                     Set membership 
length                    len                    Returns the cardinality of the set 
|                         aset | otherset        Returns a new set with all elements from both sets 
&                         aset & otherset        Returns a new set with only those elements common to both sets 
-                         aset - otherset        Returns a new set with all items from the first set not in second 
<=                        aset <= otherset       Asks whether all elements of the first set are in the second 

>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>> len(mySet)
5
>>> False in mySet
True
>>> "dog" in mySet
False

Method Name               Use                            Explanation
union                     aset.union(otherset)           Returns a new set with all elements from both sets 
intersection              aset.intersection(otherset)    Returns a new set with only those elements common to both sets 
difference                aset.difference(otherset)      Returns a new set with all items from first set not in second 
issubset                  aset.issubset(otherset)        Asks whether all elements of one set are in the other 
add                       aset.add(item)                 Adds item to the set 
remove                    aset.remove(item)              Removes item from the set 
pop                       aset.pop()                     Removes an arbitrary element from the set 
clear                     aset.clear()                   Removes all elements from the set 

>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>> yourSet = {99,3,100}
>>> mySet.union(yourSet)
{False, 4.5, 3, 100, 6, 'cat', 99}
>>> mySet | yourSet
{False, 4.5, 3, 100, 6, 'cat', 99}
>>> mySet.intersection(yourSet)
{3}
>>> mySet & yourSet
{3}
>>> mySet.difference(yourSet)
{False, 4.5, 6, 'cat'}
>>> mySet - yourSet
{False, 4.5, 6, 'cat'}
>>> {3,100}.issubset(yourSet)
True
>>> {3,100}<=yourSet
True
>>> mySet.add("house")
>>> mySet
{False, 4.5, 3, 6, 'house', 'cat'}
>>> mySet.remove(4.5)
>>> mySet
{False, 3, 6, 'house', 'cat'}
>>> mySet.pop()
False
>>> mySet
{3, 6, 'house', 'cat'}
>>> mySet.clear()
>>> mySet
set()
"""


""" Dictionary
Operation Name            Operator               Explanation
[]                        myDict[k]              Returns the value associated with k, otherwise its an error 
in                        key in adict           Returns True if key is in the dictionary, False otherwise 
del                       del adict[key]         Removes the entry from the dictionary 

Method Name               Use                    Explanation
keys                      adict.keys()           Returns the keys of the dictionary in a dict_keys object 
values                    adict.values()         Returns the values of the dictionary in a dict_values object 
items                     adict.items()          Returns the key-value pairs in a dict_items object 
get                       adict.get(k)           Returns the value associated with k, None otherwise 
get                       adict.get(k,alt)       Returns the value associated with k, alt otherwise

>>> phoneext={'david':1410,'brad':1137}
>>> phoneext
{'brad': 1137, 'david': 1410}
>>> phoneext.keys()
dict_keys(['brad', 'david'])
>>> list(phoneext.keys())
['brad', 'david']
>>> phoneext.values()
dict_values([1137, 1410])
>>> list(phoneext.values())
[1137, 1410]
>>> phoneext.items()
dict_items([('brad', 1137), ('david', 1410)])
>>> list(phoneext.items())
[('brad', 1137), ('david', 1410)]
>>> phoneext.get("kent")
>>> phoneext.get("kent","NO ENTRY")
'NO ENTRY'
"""