from mergesort import mergesort
from random import randint
import time

def gen_arr(n):
    data = []
    for i in range(n):
        data.append(randint(0, 100))
    return data

arr = gen_arr(150000)
t = time.time()
mergesort(arr)
t = time.time() - t
# print(arr)
print("**********  {}  **********".format(t))
