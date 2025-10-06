from tools.mergesort import MergeSort

class Node:
    def __init__(self, data: int, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_data(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def add_other_data(self, data):
        current = self.head
        prev_current = None
        while current:
            if current.data == data:
                if prev_current:
                    prev_current.next = current.next
                    current.next = None
                else:
                    prev_current = None
                return
            prev_current = current
            current = current.next

        new_node = Node(data, self.head)
        self.head = new_node

    @property
    def print_data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    @property
    def to_sorted_array(self):
        linked_array = []
        current = self.head
        while current:
            linked_array.append(current.data)
            current = current.next
        
        sorted_array = MergeSort.merge(linked_array)
        del linked_array
        return sorted_array



arr = "1 2 3 4 5 0 1 7 5 8 0".split()

A_array = []
B_array = []
zero_ind = False

for i in arr:
    number = int(i)
    if number == 0:
        zero_ind = True
    elif not zero_ind:
        A_array.append(number)
    else:
        B_array.append(number)

linklist = LinkedList()

for data in A_array:
    linklist.add_data(data)

for data in B_array:
    linklist.add_other_data(data)
    
print(linklist.to_sorted_array)


