#remove even number from a list
#challenge 1:REMOVE EVEN INTEGERS FROM A LIST
def remove_even(list):
    return[item for item in list if item % 2 != 0]
my_list = [12,67,89,0,98,98,56,73,45]
print(remove_even(my_list))

#MERGE TWO SORTED LISTS
def merge_lists(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1
print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))

#challenge3: FIND TWO NUMBERS THAT ADD UP TO K
def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False
print(find_sum([1, 2, 3, 4], 5))
#CHALLENGE4: FIND TWO NUMBERS THAT ADD UP TO "K"

def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


print(find_product([1, 2, 3, 4]))

#challenge5: FIND MINIMUN VALUE IN LIST
def find_minimum(arr):
    minimum = arr[0]
    # At every Index compare its value with minimum and if its less
    # then make that index value new minimum value
    for val in arr:
        if val < minimum:
            minimum = val

    return minimum

print(find_minimum([9, 2, 3, 6]))

#Challenge 6: First Non-Repeating Integer in a list
def find_first_unique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    counts = counts.fromkeys(lst, 0)
    for ele in lst:
        counts[ele] += 1  # Incrementing for every repitition
    for ele in lst:
        if counts[ele] <= 1:
            return ele
    return None

print(find_first_unique([9, 2, 3, 2, 6, 6]))

#Challenge 7: Find Second Maximum Value in a List


def find_second_maximum(lst):
    firstMax = float('-inf')
    secondMax = float('-inf')
    # find first max
    for item in lst:
        if item > firstMax:
            firstMax = item
    # find max relative to first max
    for item in lst:
        if item != firstMax and item > secondMax:
            secondMax = item
    return secondMax


print(find_second_maximum([9, 2, 3, 6]))

#Challenge 8: Right Rotate List
def right_rotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
print(right_rotate([10, 20, 30, 40, 50], abs(3)))

#Challenge 9: Rearrange Positive & Negative Values

def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
#Challenge 10: Rearrange Sorted List in Max/Min Form

def max_min(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        # Append corresponding last element
        result.append(lst[-(i+1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result


print(max_min([1, 2, 3, 4, 5, 6, 7]))

