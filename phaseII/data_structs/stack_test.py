from stack import Element, LinkedList, Stack

el1 = Element("Apple")
el2 = Element("Peach")
el3 = Element("Orange")
el4 = Element("Grapes")
el5 = Element("Kiwi")

stack = Stack()
stack.push(el1)
stack.push(el2)
print(f"\n{stack.pop().value} was popped out of the stack\n")
stack.push(el2)
stack.push(el3)
stack.push(el5)
stack.push(el4)

print(stack.ll.toArray())

try:
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
    print(f"\n{stack.pop().value} was popped out of the stack\n")
except Exception:
    print("Pop operation was not carried out!")

print(stack.ll.toArray())