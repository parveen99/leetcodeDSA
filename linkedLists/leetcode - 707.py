class SinglyLL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_head(self, val):
        new_node = SinglyLL(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_tail(self, val):
        new_node = SinglyLL(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
        curr.next = new_node
        new_node.next = None 
        self.size += 1

    def add_at_index(self, val, index):
        if index < 0 or index > self.size:
            return 
        new_node = SinglyLL(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def get_val_at_index(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        print(curr.val)


    def print_all_values(self):
        curr = self.head
        while curr is not None:
            print(curr, end = '->')
            curr = curr.next









ll_obj = MyLinkedList()
ll_obj.add_at_head(1)
ll_obj.add_at_head(4)
ll_obj.add_at_head(53)
ll_obj.add_at_tail(89)
ll_obj.add_at_index(2,2)
ll_obj.get_val_at_index(2)
ll_obj.print_all_values()























# class SinglyLL:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)


# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def add_at_head(self, val):
#         new_node = SinglyLL(val)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1

#     def print_all_values(self):
#         curr = self.head
#         elements = []
#         while curr is not None:
#             elements.append(str(curr))
#             curr = curr.next
#             print(elements)


# ll_obj = MyLinkedList()
# ll_obj.add_at_head(3)
# ll_obj.add_at_head(4)
# ll_obj.print_all_values()
