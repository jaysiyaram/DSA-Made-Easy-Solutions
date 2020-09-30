class NodeTypeError(Exception):
    "The data supplied is not an instance of class Node or None"
    pass


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __eq__(self, node1):
        if node1:
            return self.data == node1.data
    
    @property
    def data(self):
        # print("Getting value...")
        return self._data

    @data.setter
    def data(self, value):
        # print("Setting value...")
        self._data = value

    @property
    def next_node(self):
        # print("Getting next_node node...")
        return self._next_node

    @next_node.setter        
    def next_node(self, value):
        # print("Setting next_node node...")
        self._next_node = value

    def has_next_node(self):
        return self.next_node != None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    @property
    def head(self):
        # print("Getting head...")
        return self._head

    @head.setter
    def head(self, value):
        # print("Setting head...")
        if isinstance(value, Node) or value == None:
            self._head = value
        else:
            raise NodeTypeError

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, "> ", end="")
            current = current.next_node
        print(None)

    def list_length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next_node
        return count

    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head != None:
            node.next_node = self.head
            self.head = node
        else:
            self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = node

    def insert_multiple_data(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_position(self, data, pos):
        ll_length = self.list_length()
        if pos < 0 or pos > ll_length + 1:
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        else:
            node = Node(data)
            current = self.head
            count = 1
            while count < pos-1:
                count += 1
                current = current.next_node
            node.next_node = current.next_node
            current.next_node = node

    def delete_from_beginning(self):
        if not self.list_length():
            print("This list is empty")
        else:
            self.head = self.head.next_node

    def delete_from_end(self):
        if not self.list_length():
            print("This list is empty")
        current = self.head
        prev = self.head
        while current.next_node != None:
            prev = current
            current = current.next_node
        prev.next_node = None

    def delete_node(self, node):
        current = self.head
        prev = None
        found = False
        # import pdb; pdb.set_trace()
        while not found:
            if current == node:
                found = True
            elif current == None:
                raise ValueError("The node is not present in the list")
            else:
                prev = current
                current = current.next_node
        if prev is None:
            self.head = current.next_node
        else:
            prev.next_node = current.next_node

    def delete_value(self, value):
        current = self.head
        prev = None
        while current.next_node != None or current.data == value:
            if current.data == value:
                if not prev:
                    self.head = current.next_node
                else:
                    prev.next_node = current.next_node
                return
            else:
                prev = current
                current = current.next_node
        print("The value is not present in the list")

    def delete_at_position(self, pos):
        current = self.head
        prev = None
        count = 0
        if pos < 0 or pos > self.list_length():
            print('Invalid postion')
            return
        while current.next_node != None or count < pos:
            count += 1
            if count == pos:
                if not prev:
                    self.head = current.next_node
                else:
                    prev.next_node = current.next_node
                return
            else:
                prev = current
                current = current.next_node


# Sample code --
node = Node(12)
print("This is next_node value of the node", node.next_node)
print("Does this node have a next_node node", node.has_next_node())


# Trigger code of linked list --
llist = LinkedList(node)
llist.insert_multiple_data([13, 14, 15, 16])
llist.print_list()
print("The length of the list is", llist.list_length())
llist.insert_at_beginning(11)
print(llist.list_length())
llist.insert_at_position(50, 7)
llist.print_list()


# Trigger code for deletion of the node --
llist.delete_from_beginning()
llist.print_list()
llist.delete_from_end()
llist.print_list()
llist.delete_at_position(1)
llist.print_list()
llist.delete_value(12)
llist.print_list()
llist.delete_node(Node(13))
llist.print_list()
