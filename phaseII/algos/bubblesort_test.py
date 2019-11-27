import time
from random import randint
from bubblesort import bubblesort

def gen_arr(n):
    data = []
    for _i in range(n):
        data.append(randint(0, 100))
    return data
        
arr = gen_arr(1000)

start_time = time.time()    
bubblesort(arr)
endtime = time.time() - start_time
print("\n",arr)
print("--- %s seconds ---" % endtime)