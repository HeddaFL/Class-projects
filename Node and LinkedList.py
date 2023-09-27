
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_node_list(self):
        self.node = self.head 
        self.node_list_first = []
        self.node_list_last = []

        while self.node is not None:
            self.node_list_first.append(self.node.data)
            self.node = self.node.next
        
        while self.node is not None:
            self.node_list_last.append(self.node.data)
            self.node = self.node.next
        
        final_output_first = "".join(self.node_list_first)
        final_output_last = "".join(self.node_list_last)
        self.final_output = final_output_first + final_output_last
        print(f'{self.final_output}')

    
    def add(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else: 
            last_node = self.head

            while last_node.next is not None:
                last_node = last_node.next
        
            last_node.next = new_node


my_node_list = LinkedList()
my_node_list.add('H')
my_node_list.add('E')
my_node_list.add('D')
my_node_list.add('D')
my_node_list.add('A')
my_node_list.add(' ')
my_node_list.add('L')
my_node_list.add('A')
my_node_list.add('U')
my_node_list.add('P')
my_node_list.add('S')
my_node_list.add('T')
my_node_list.add('A')
my_node_list.add('D')

my_node_list.print_node_list()
