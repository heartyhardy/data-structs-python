class Element(object):
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self, head=None):
        self.head=head

    
    def append(self, new_element):
        current = self.head

        if(self.head):
            while(current.next):
                current = current.next
            current.next = new_element
        else:
            self.head=new_element
    
    def get(self, pos):

        rpos = 1
        current = self.head

        while(current and rpos <= pos):
            if(rpos is pos):
                return current
            current = current.next
            rpos += 1
        return None
    
    def insert(self, element, pos):

        rpos = 1
        current = self.head

        if(pos == 1):
            element.next = self.head
            self.head=element
            return
        else:
            while(current and rpos < pos):
                if rpos is pos -1:
                    element.next = current.next
                    current.next = element
                current = current.next
                rpos +=1


    def delete(self, value):

        current = self.head
        previous = None

        while current.value != value and current.next:
            
            previous = current
            current = current.next

            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next


ll = LinkedList()
el = Element(5)
el2 = Element(10)
el3 = Element(15)

ll.append(el)
ll.append(el2)
ll.insert(el3, 1)
ll.delete(15)

current = ll.head
while(current):
    print(current.value)
    current= current.next
