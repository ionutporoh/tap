list = []
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0,n):
    print("Insert element for: ", i, " ")
    item = int(input())
    list.append(item)
print("The list is", list)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
# print("Sorted list is:", list)


def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)



size = len(list)

quickSortList = list
 
quickSort(quickSortList, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(list)