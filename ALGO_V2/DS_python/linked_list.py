# linked list: a chain of node object.
# node: value + pointer(to the next node)
# head pointer to the first node
# tail pointer to the null

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# join the node to get a linked list
# linked list class with a single head pointer

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def unshift(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return data

        template_node = self.head
        self.head = new_node
        new_node.next = template_node
        return data

    def find(self, data):
        #     find the first node by its data value
        if self.head == None:
            return None

        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def size(self):

        if not self.head:
            return None

        length = 0
        current_node = self.head
        while current_node.next:
            length += 1
            current_node = current_node.next

        return length + 1

    def print(self):
        print_node = self.head
        while print_node:
            print(print_node.data)
            print_node = print_node.next


first_ll = LinkedList()  # linked list object
second_node = Node(4)
first_ll.head = Node(3, second_node)
first_ll.push(10)
first_ll.unshift(88)
# first_ll.print()
first_ll.find(10).next = Node(67)
first_ll.print()
size = first_ll.size()
print(size)
