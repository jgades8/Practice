
def one_away(str1: str, str2: str):
    if str1 == str2:
        return True
    if abs(len(str1)-len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        changes = False
        for i in range(0, len(str1)):
            if str1[i] == str2[i]:
                continue
            else:
                if changes:
                    return False
                else:
                    changes = True
        return True
    elif len(str1) > len(str2):
        changes = False
        i = 0
        for char in str2:
            if char == str1[i]:
                i += 1
            else:
                if changes:
                    return False
                else:
                    if char != str1[i+1]:
                        return False
                    i += 2
                    changes = True
        return True
    elif len(str2) > len(str1):
        changes = False
        i = 0
        for char in str1:
            if char == str2[i]:
                i += 1
            else:
                if changes:
                    return False
                else:
                    if char != str2[i+1]:
                        return False
                    i += 2
                    changes = True
        return True


if __name__ == '__main__':
    print(one_away('pale', 'ple'))
    print(one_away('pale', 'she'))
    print(one_away('pale', 'pales'))
    print(one_away('pale', 'pane'))
    print(one_away('pale', 'bake'))
