# Used for finding index of a specific value in a SORTED array
# Splits array in half, low and high, and compares to midpoint
# Does this recursively

def binary_search(arr: [], low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] is x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1  # value is not in array


if __name__ == '__main__':
    arr = [0, 2, 3, 4, 6, 7, 12, 14, 19, 25]
    print(binary_search(arr, 0, len(arr) - 1, 3))
    print(binary_search(arr, 0, len(arr) - 1, 12))
    print(binary_search(arr, 0, len(arr) - 1, 0))
    print(binary_search(arr, 0, len(arr) - 1, 25))
