# Determine if a string has all unique characters
# What if you can't use additional data structures

MAX_NUM_CHARS = 256


def is_unique(string: str):
    # If we know the maximum number of chars available, we can check if length of string is more
    if len(string) > MAX_NUM_CHARS:
        return False
    char_arr = []
    for char in string:
        if char in char_arr:
            return False
        else:
            char_arr.append(char)
    return True


if __name__ == '__main__':
    print(is_unique("potato"))
    print(is_unique("unique"))
    print(is_unique("thisedrf"))
    print(is_unique("0965dhu"))
