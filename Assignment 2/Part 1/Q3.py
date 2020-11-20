import multiprocessing as mp

list_c = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]

def normalize_2d_array(list_c):
    min = min(list_c)
    max = max(list_c)
    return [(i - min)/(max-min) for i in list_c]

pool = mp.Pool(mp.cpu_count())
results = [pool.apply(normalize_2d_array, args=(l1, )) for l1 in list_c]
pool.close()    
print(results[:10])