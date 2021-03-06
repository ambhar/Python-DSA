## This is a function to check if an Array is sorted using RECURSION

def isArraySorted(array):
    print(array)
    if len(array)==1:
        return True
    return array[0] <= array[1] and isArraySorted(array[1:])# It will check first two elements are sorted and if not
                                                            # then will call function with array starting from second element

myArray =[4,7,8,10,16,12,9,13,10,15]
print(isArraySorted(myArray))

# Time Complexity is O(n) 
# Space Complexity is O(n) for recursive stack space 

# array[1:] means starting from index 1 to end
# array[1:5] means starting from index 1 to index 5 of array