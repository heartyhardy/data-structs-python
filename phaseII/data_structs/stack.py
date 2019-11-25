class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    
    def append(self, element):
        current = self.head

        element.next = current
        self.head = element
    

    def remove(self):
        current = self.head

        if current:
            self.head = self.head.next
        return current

    
    def toArray(self):
        current = self.head
        result = []

        while current:
            result.append(current.value)
            current = current.next
        return result


class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    
    def push(self, element):
        self.ll.append(element)
    
    def pop(self):
        return self.ll.remove()
