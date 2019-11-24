class Element(object):
    def __init__(self, value):
        self.value=value
        self.next=None
    
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    
    def append(self, element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element
    

    def insert_top(self, element):
        element.next = self.head
        self.head = element
    

    def delete_top(self):
        if self.head:
            deleted = self.head
            nextelement = deleted.next
            self.head = nextelement
            return deleted
        else:
            return None


class Stack(object):
   
    def __init__(self, top = None):
        self.ll = LinkedList(top)


    def push(self, element):
        self.ll.insert_top(element)

    def pop(self):
        return self.ll.delete_top()


el1 = Element(5)
el2 = Element(10)
el3 = Element(15)


stk = Stack()
stk.push(el1)
stk.push(el2)
stk.push(el3)

print(stk.pop().value)
print(stk.pop().value)
print(stk.pop().value)





