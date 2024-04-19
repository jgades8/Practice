# Find Kth to last element

from LinkedList import Node, LinkedList


def kth_to_last_element(linked_list: LinkedList, from_end: int):
    # get length
    length = linked_list.length
    # find xth element (x = length - k)
    from_start = length - from_end
    # range is NOT inclusive, does it get right value??
    current = linked_list.head
    for i in range(from_start):
        current = current.next # check that this exists?
    return current.data


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append_to_tail(3)
    list1.append_to_tail(1)
    list1.append_to_tail(5)
    list1.append_to_tail(7)
    list1.append_to_tail(13)
    list1.append_to_tail(6)
    print(kth_to_last_element(list1, 4))
