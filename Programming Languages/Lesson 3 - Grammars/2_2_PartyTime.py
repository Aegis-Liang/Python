# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def list_all(ls):
    if len(ls) == 0:
        return []
    elif len(ls) == 1:
        return [ls[0]] + [[]]
    else:
        # use one half map(lambda x:[[]] + [x], list_all(ls[1:]))  or the other to debug
        return map(lambda x:[ls[0]]+[x], list_all(ls[1:])) + map(lambda x:[[]] + [x], list_all(ls[1:])) 
        
print list_all(['a', 'b'])



def sublists(big_list, selected_so_far):
    if big_list == []:
        print selected_so_far
    else:
        current_element = big_list[0]
        rest_of_big_list = big_list[1:]
        sublists(rest_of_big_list, selected_so_far + [current_element])
        sublists(rest_of_big_list, selected_so_far)
        
dinner_guests = ["LM", "ECS", "SBA"]
sublists(dinner_guests, [])

def sublists_total(big_list, selected_so_far):
    if big_list == []:
        return [selected_so_far]
    else:
        current_element = big_list[0]
        rest_of_big_list = big_list[1:]
        return sublists_total(rest_of_big_list, selected_so_far + [current_element]) + sublists_total(rest_of_big_list, selected_so_far)
print sublists_total(dinner_guests, [])
