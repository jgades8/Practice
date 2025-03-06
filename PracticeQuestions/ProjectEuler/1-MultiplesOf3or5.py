# If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6, 9
# The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000

def find_sum(max: int):
    total = sum(x for x in range(max) if (x % 3 == 0 or x % 5 == 0))
    return total


if __name__ == '__main__':
    max = 1000
    find_sum(max)
    