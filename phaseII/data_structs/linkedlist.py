"""
*** Element which can be inserted into the Linkedlist ***
"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

"""
*** Linked List class, contains the head of the list and
*** contains the functions to append, get and delete elements
"""
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    """
    *** Appends a new element to the list. If head is None,
    *** new element will be set as head
    """
    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    

    """
    *** Fetches an element at the given position. If the position does not
    *** exist returns None
    """
    def get(self, pos):
        cursor = 0
        current = self.head

        if pos == 0:
            return self.head
        else:
            while current.next:
               
                current = current.next
                cursor += 1

                if cursor == pos:
                    return current

            return None
    

    """
    *** Inserts an element to the Linkedlist at the given position.
    *** If the position does not exists throws an error
    """
    def insert(self, element, pos):
        current = self.head
        cursor = 0

        if pos == 0:
            return self.head
        
        while current.next:
            previous = current
            current = current.next
            cursor += 1

            if cursor == pos:
                previous.next = element
                element.next = current
                return
        current.next = element
        return None


    """
    *** Deletes an element at the given position
    """
    def delete(self, pos):
        current = self.head
        cursor = 0

        if pos == 0 and current.next:
            self.head = current.next
            return
        elif pos == 0 and not current.next:
            self.head = None
            return
        else:
            while current.next:
                previous = current
                current = current.next
                cursor += 1

                if cursor == pos:
                    previous.next = current.next
                    current = None
                    return


    """
    *** Clears out the Linked list
    """
    def clear(self):
        current = self.head
        
        if not current:
            self.head = None
            return
        
        while current:
            previous = current
            current = previous.next
            previous = None



