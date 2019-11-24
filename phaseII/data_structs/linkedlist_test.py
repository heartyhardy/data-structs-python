from linkedlist import LinkedList, Element

el1 = Element("Apple")
el2 = Element("Orange")
el3 = Element("Pear")

ll = LinkedList(head=None)
ll.append(el1)
ll.append(el2)
ll.append(el3)

print(ll.get(0).value)
print(ll.get(1).value)
print(ll.get(2).value)
print(ll.get(3))

