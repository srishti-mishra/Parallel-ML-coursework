import numpy as np
import multiprocessing as mp
import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[100000, 1000])
data = arr.tolist()
#data[:5]
start = time.time()
def examp01(row, minimum=4, maximum=8):
    """Returns how many numbers between `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count
# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(4)
# Step 2: `pool.apply` the `examp01()`
results = [pool.apply(examp01, args=(row, 4, 8)) for row in data]

#Step 3 Close Pool
pool.close()
print('Pool.apply execution:', results[:10])
print(f'Execution Time pool.starmap(): {time.time() - start} seconds')

