# create a node for link_list
class node:
    def __init__(self, data_avl=None):
        self.data_avl = data_avl
        self.next_avl = None

class SLinked_list:
    def __init__(self):
        self.top_avl = None

    # adding new node at the begining
    def In_beg(self, new_data):
        new_node = node(new_data)
        # update the list
        new_node.next_avl = self.top_avl
        self.top_avl = new_node

    # removing the node
    def remove_node(self, remove_key):

        remove = self.top_avl

        if (remove is not None):
            if (remove.data_avl == remove_key):
                self.top_avl = remove.next_avl
                remove = None
                return

        while (remove is not None):
            if remove.data_avl == remove_key:
                break
            rev = remove
            remove = remove.next_avl

        if (remove == None):
            return

        rev.next_avl = remove.next_avl

        remove = None

    # traversing the link_list
    def list_print(self):
        print_avl = self.top_avl
        while (print_avl):
            print(print_avl.data_avl)
            print_avl = print_avl.next_avl

# Main function to initalize the recursion #
list = SLinked_list()
list.top_avl = node("Mon")
e2 = node("Tue")
e3 = node("Wed")
list.top_avl.next_avl = e2
e2.next_avl = e3

list.In_beg("Sun")
list.remove_node("Wed")

# print the traversing_elements
list.list_print()

