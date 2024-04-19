# Sorts an array using list comprehension
# Picks a pivot point and compares all values to it
# placing smaller values in one array and bigger in another

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    arr = [3, 17, -4, 89, 7, 2, 5, 3]
    print(quick_sort(arr))
