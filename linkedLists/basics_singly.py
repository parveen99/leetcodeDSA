
class SinglyLL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


head = SinglyLL(4)
A = SinglyLL(5)
B = SinglyLL(8)
C = SinglyLL(12)

head.next = A
A.next = B
B.next = C


def print_all_values_singlyll(head):
    curr = head
    while curr is not None:
        print(curr)
        curr = curr.next


print_all_values_singlyll(head)


def display_singly_ll(head):
    '''    
    curr = head
    while curr is not None:
        print(curr, end = '->')
        curr = curr.next
    '''

    ele = []
    curr = head
    while curr is not None:
        value = str(curr.val)
        ele.append(value)
        curr = curr.next
    print(' -> '. join(ele))


display_singly_ll(head)



def if_val_exist_in_singly(head, val):
    curr = head
    while curr is not None:
        if(val == curr.val):
            return True
        curr = curr.next
    return False


print(if_val_exist_in_singly(head, 2))

def get_val_at_index(index, head):
    if (index == 1):
        return str(head.val)
    el

print(get_val_at_index(2)) #-> 5



class DoublyLL:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)
