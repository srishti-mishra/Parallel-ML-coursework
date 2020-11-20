
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

pool = mp.Pool(4)

results = pool.starmap(examp01, [(row, 4, 8) for row in data])

pool.close()
print('Pool.apply execution:', results[:10])
print(f'Execution Time pool.apply(): {time.time() - start} seconds')

