# iterative search
def search(haystack, needle):
    c = 0
    for e in haystack:
        if (int(e) == int(needle)):
            return c
        c += 1
    return False


# binary search
listPos = []


def binarySearch(haystack, needle, low, high):
    if high >= low:
        mid = (high + low) // 2

        # lucky find
        if int(haystack[mid]) == int(needle):
            listPos.append(mid)
            # remove found element and try again
            haystack.remove(haystack[mid])
            return binarySearch(haystack, needle, 0, len(number_list) - 1)
        # lower than middle
        # recursive run
        elif haystack[mid] > needle:
            return binarySearch(haystack, needle, low, mid - 1)
        # higher than
        # recursive run
        else:
            return binarySearch(haystack, needle, mid + 1, high)

    else:
        # we didn't find
        return -1


# input data
number_list = []
needle = int(input("element to find: "))
print("\n")
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0, n):
    print("Insert element for: ", i, " ")
    item = int(input())
    number_list.append(item)
print("The list is", number_list)


# output data
find = search(number_list, needle)

if find != False:
    print("we found element on pos: ", find)
else:
    print("we didn't find the element: ", needle)

# order list asc for binary search
number_list.sort()
bSearch = binarySearch(number_list, needle, 0, len(number_list)-1)

print(listPos)

if len(listPos) == 0:
    print("binary search did not found element")
else:
    print("binary search EVRIKA!!!! We found element {0} times".format(
        len(listPos)))
