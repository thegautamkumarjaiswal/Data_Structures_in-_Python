# create a node of list #
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a list #
class Create_list:
    def __init__(self):
        self.head = node(None)
        self.end = node(None)
        self.head.next = self.end
        self.end.next = self.head

    # insertion in begining #
    def in_beg(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            new_node.next = self.head
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.end.next = self.head

    # deletion function in end #
    def delete_at_end(self):
        if self.head == None:
            return
        else:
            if self.head != self.end:
                current = self.head
                while current.next != self.end:
                    current = current.next
                self.end = current
                self.end.next = self.head
            else:
                self.head = self.end = None

    # display function for display the linked list #
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Adding node to the start of the list.\n")
            print(current.data)
            while current.next != self.head:
                current = current.next
                print(current.data)
            print("\n")

# create circular linked list to inisilaize the function #
class Circular_linkedlist:
    cl = Create_list()
    cl.in_beg("> College Name")
    cl.display()
    cl.in_beg("> Address")
    cl.display()
    cl.in_beg("> Phone Number")
    cl.display()
    cl.in_beg("> College Email-id")
    cl.display()
    cl.delete_at_end()
    cl.display()
    cl.delete_at_end()
    cl.display()
    cl.delete_at_end()
    cl.display()

