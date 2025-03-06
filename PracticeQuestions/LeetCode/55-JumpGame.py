
def jump_game(arr: [int]):
    if len(arr) == 1 or 0 not in arr:
        return True
    index = 0
    while index < (len(arr)-1):
        curr_jump, next_jump, max_jump = 0, 0, 0
        for jump_length in range(1, arr[index]+1):
            if index + jump_length > len(arr) - 1:
                return True
            if jump_length + arr[index+jump_length] > max_jump:
                curr_jump = jump_length
                max_jump = jump_length + arr[index+jump_length]
        if curr_jump == 0:
            return False
        index += curr_jump
    return True


if __name__ == '__main__':
    print(jump_game([2, 3, 1, 1, 4]))
    print(jump_game([2, 2, 1, 0, 4]))
    print(jump_game([2]))
    print(jump_game([2, 2, 0, 1, 4, 5, 2, 1]))
