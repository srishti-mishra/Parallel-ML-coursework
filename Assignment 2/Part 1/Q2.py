import os                                                                       
import multiprocessing as mp

processes = ('script1.py', 'script2.py', 'script3.py')                      

def run_python(process):                                                             
    os.system('python {}'.format(process))                                      

pool = mp.Pool(processes=3)                                                        
pool.map(run_python, processes) 