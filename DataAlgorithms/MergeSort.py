# Sorts an array by separating into pieces
# Then merges them by having pointers in each array and final array
# comparing each value and placing lower value in final array

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # Now merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [3, 17, -4, 89, 7, 2, 5, 3]
    merge_sort(arr)
    print(arr)
