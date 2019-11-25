from deque import Element, LinkedList, Deque

el1 = Element("Apple")
el2 = Element("Peach")
el3 = Element("Orange")
el4 = Element("Pear")
el5 = Element("Kiwi")

dq = Deque()

dq.enqueue(el3)
dq.push(el2)
dq.enqueue(el1)
dq.push(el4)
dq.enqueue(el5)

print(dq.ll.toArray())

dq.pop()
dq.dequeue()
dq.dequeue()
dq.pop()


print(dq.ll.toArray())
