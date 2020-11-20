import multiprocessing, os										
import matplotlib.pyplot as plt                                
from sklearn import svm                                         
import numpy as np                                              
from time import time                                           

def foo(i):
    print ('called function in process: %s' %i)
    print(os.getpid())
    return

def cvkfold(X, y, tuning_params, partitions, k):
    '''uses kfolds to cross validate training and test datasets'''
    n_tuning_params = tuning_params.shape[0]                                
    partition = partitions[k]                                               
    
  
    Train = np.delete(np.arange(0, X.shape[0]), partition)                  
    
    Test = partition                                                        
    X_train = X[Train, :]                                                   
    y_train = y[Train]
    X_test = X[Test, :]
    y_test = y[Test]
    accuracies = np.zeros(n_tuning_params)                                  
    for i in range(0, n_tuning_params):                                     
        svc = svm.SVC(C = tuning_params[i], kernel = "linear")              
        accuracies[i] = svc.fit(X_train, y_train).score(X_test, y_test)     
    return(accuracies)


def process_svc( kfolds, X, y):
    '''uses parallel cpus to cross validate best hyperplane with process'''
    tuning_params = np.logspace(-6, -1, 10)                                
    partitions = np.array_split(np.random.permutation([i for i in range(0, X.shape[0])]), kfolds)

    jobs = []

    for k in range(0, kfolds):   
        process = multiprocessing.Process(target = cvkfold, args = (X, y, tuning_params, partitions, k))
        jobs.append(process)

    for process_job in jobs:
        process_job.start()

    for process_job in jobs:
        process_job.join()

if __name__=='__main__':

    test = np.loadtxt("optdigits.txt", delimiter = ",")
    X = test[:, 0:64]                                                       
    y = test[:, 64]                                                         
    kfolds = 5
    t1 = time()
    
    process_svc(kfolds, X, y)
    # best_tuning_param = parallel_tuning_process(cpu_count, kfolds, X, y)     
    # print('Best tuning param %0.6f.'% best_tuning_param)  
    elapsed = (time() - t1)
    print('Process runs in %0.9f seconds.' % (elapsed))               
    