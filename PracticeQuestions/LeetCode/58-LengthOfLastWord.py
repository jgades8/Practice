
def lengthOfLastWord(s: str) -> int:
    str_arr = s.split()
    # while len(str_arr[-1]) == 0:
    #     str_arr.pop()
    return len(str_arr[-1])


if __name__ == '__main__':
    print(lengthOfLastWord("  some test  string  a "))
