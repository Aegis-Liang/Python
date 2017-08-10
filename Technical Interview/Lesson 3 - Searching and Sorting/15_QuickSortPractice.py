"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    quicksort_helper(array, 0, len(array) -1 )

    
def quicksort_helper(array, start, end):
    if start < end:
        pivot_index = partion(array, start, end)
        
        #middle = (start + end)//2
        quicksort_helper(array, start, pivot_index - 1)
        quicksort_helper(array, pivot_index + 1, end)

def partion(array, start, end):
    pivot = array[start]
    
    leftmark = start + 1
    rightmark = end
    
    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivot:
            leftmark += 1
            
        while leftmark <= rightmark and array[rightmark] >= pivot:
            rightmark -= 1
            
        if rightmark < leftmark:
            done = True
        else:
            array[leftmark], array[rightmark] = array[rightmark], array[leftmark]
    
    array[start], array[rightmark] = array[rightmark], array[start]
    return rightmark        
        
              
                
"""            
from random import randrange


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in xrange(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)     
"""    
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
print test