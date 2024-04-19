
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append_to_tail(self, data: int):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.length += 1

    def print_list(self):
        node = self.head
        print(node.data)
        while node.next:
            node = node.next
            print(node.data)
