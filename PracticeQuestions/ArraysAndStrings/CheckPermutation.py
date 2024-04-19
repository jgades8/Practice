# Given 2 strings, determine if one is a permutation of the other

def is_permutation(str1: str, str2: str):
    # to consider: does space matter?? capitals??
    # check if length matches
    if len(str1) != len(str2):
        return False
    # sort strings and compare
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    if sorted1 == sorted2:
        return True
    return False


if __name__ == '__main__':
    print(is_permutation("abba", "abab"))
    print(is_permutation("askdfs", "qaswed"))
