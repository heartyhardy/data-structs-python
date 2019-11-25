class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head = None):
        self.head = head
        self.tail = self.head
        


    def append(self, operation, element):

        # enqueue from tail
        if operation is 1:
            current = self.tail
            if current:
                current.next = element
                self.tail = element
            else:
                self.tail = element
                self.head = element
                
        # enqueue from head
        elif operation is 2:
            current = self.head
            tail = self.tail

            if current:
                element.next = current
                self.head = element

                if tail == None:
                    self.tail = current

            else:
                element.next = self.tail
                self.tail = element
                self.head = element
        else:
            pass

    def remove(self, operation):

        # dequeue from head
        if operation is 1:
            current = self.head

            if current:
                self.head = self.head.next

                if self.head == self.tail:
                    self.tail = self.head

                return current

            else:
                self.tail = None
                return None
        
        # dequeue from tail
        elif operation is 2:
            current = self.head

            if current is self.tail:
                self.head = None
                self.tail = None
                return
            
            if current:
                while current:                
                    previous = current
                    current = current.next

                    if current is self.tail:
                        self.tail = None
                        self.tail = previous
                        previous.next = None

            else:
                self.tail = None
                return None

    def toArray(self):
        current = self.head
        result = []

        while current:
            result.append(current.value)
            current = current.next
        return result


class Deque(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    
    def enqueue(self, element):
        self.ll.append(1, element)
    
    def push(self, element):
        self.ll.append(2, element)

    def dequeue(self):
        self.ll.remove(1)    

    def pop(self):
        self.ll.remove(2)
