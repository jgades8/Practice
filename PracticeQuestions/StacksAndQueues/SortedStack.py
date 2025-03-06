# Sort a stack with the lowest on top
# Can use one additional stack

def sort_stack(stack):
    tmp_stack = []
    while stack:
        tmp = stack.pop()
        while True:
            if tmp_stack:
                if tmp >= tmp_stack[len(tmp_stack)-1]:
                    tmp_stack.append(tmp)
                    break
                else:
                    stack.append(tmp_stack.pop())
            else:
                tmp_stack.append(tmp)
                break
    while tmp_stack:
        stack.append(tmp_stack.pop())
    return stack


if __name__ == '__main__':
    stack = [3, 6, 1, 2, 7]
    stack2 = [0, 0, -12, 4, 1, 2]
    print(sort_stack(stack))
    print(sort_stack(stack2))
