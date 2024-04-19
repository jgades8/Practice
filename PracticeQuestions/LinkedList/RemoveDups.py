# Write code to remove duplicates from an unsorted Linked List

from LinkedList import Node, LinkedList


def remove_dupes(linked_list: LinkedList):
    data_arr = []
    current = linked_list.head
    data_arr.append(current.data)
    while current.next:
        if current.next.data in data_arr:
            print("removing")
            # Is this the last element?
            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None
                break
        current = current.next


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append_to_tail(3)
    list1.append_to_tail(1)
    list1.append_to_tail(5)
    list1.append_to_tail(3)
    list1.append_to_tail(13)
    list1.append_to_tail(3)
    LinkedList.print_list(list1)
    remove_dupes(list1)

    print("after removal")
    LinkedList.print_list(list1)
