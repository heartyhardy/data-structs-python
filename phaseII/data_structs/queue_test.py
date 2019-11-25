from queue_ import Element, LinkedList, Queue

el1 = Element("Apple")
el2 = Element("Pear")
el3 = Element("Peach")

q = Queue()
q.enqueue(el1)
q.enqueue(el2)

print(q.ll.toArray())

q.dequeue()
q.dequeue()
q.dequeue()


print(q.ll.toArray())

q.enqueue(el1)
q.enqueue(el2)
q.enqueue(el3)

print(q.ll.toArray())

