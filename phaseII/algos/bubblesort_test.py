import time
from random import randint
from bubblesort import bubblesort

def gen_arr():
    data = []
    for i in range(1000):
        data.append(randint(0, 100))
    return data
        
arr = gen_arr()

start_time = time.time()    
bubblesort(arr)
endtime = time.time() - start_time
print("\n",arr)
print("--- %s seconds ---" % endtime)