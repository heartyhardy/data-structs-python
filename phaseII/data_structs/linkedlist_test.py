from linkedlist import LinkedList, Element

el1 = Element("Apple")
el2 = Element("Orange")
el3 = Element("Pear")
el4 = Element("Kiwi")
el5 = Element("Mango")

ll = LinkedList(head=None)
ll.append(el1)
ll.append(el2)
ll.append(el3)
ll.insert(el4, 1)
ll.insert(el5, 4)

# print(ll.get(0).value)
# print(ll.get(1).value)
# print(ll.get(2).value)
# print(ll.get(3).value)
# print(ll.get(4).value)

current = ll.head
while current:
    print(current.value)
    current = current.next

