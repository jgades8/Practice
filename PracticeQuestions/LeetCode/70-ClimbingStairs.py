# Using recursion
def count(num_steps: int):
    if num_steps == 0:
        return 1
    elif num_steps < 0:
        return 0
    return count(num_steps-2) + count(num_steps-1)


if __name__ == '__main__':
    n = 3
    print(count(4))
