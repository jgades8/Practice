# Given an array of integers sorted in ascending order
# find indexes of the 2 nums that add to target value

def find_indexes(arr: [], target: int):
    # right pointer starts at arr[-1]
    # left pointer starts at arr[0]
    i, j = 0, (len(arr) - 1)
    high = arr[j]
    low = arr[i]
    sum = high + low
    while sum != target and i < j:
        if sum < target:
            i += 1
            low = arr[i]
        if sum > target:
            j -= 1
            high = arr[j]
        sum = low + high

    # Add 1 because first index should be 1 not 0
    print(f"{i+1} {j+1}")


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 7, 10, 11]
    target = 9
    find_indexes(arr, target)
