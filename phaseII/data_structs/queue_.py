"""
Implement using a linked list
    Can Enqueue from tail
    Can Dequeue from head
    Can Peek the head element
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.tail = self.head

    
    def append(self, element):
        
        if self.tail:
            current = self.tail
            current.next = element
            self.tail = element
        else:
            self.tail = element
            self.head = element

    def remove(self):
        if self.head:
            current = self.head
            self.head = self.head.next
            return current
        else:
            self.tail = None
            return None

    def toArray(self):
        result = []
        current = self.head

        while(current):
            result.append(current.value)
            current = current.next
        return result


class Queue(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    
    def enqueue(self, element):
        self.ll.append(element)

    def dequeue(self):
        return self.ll.remove()
    
