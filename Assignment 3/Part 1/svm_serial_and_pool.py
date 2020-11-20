import matplotlib.pyplot as plt                                 
from sklearn import svm                                         
import multiprocessing as mp                                    
import numpy as np                                              
from time import time                                           

def plot_digits(X, y):
    '''Plot some of the digits'''
    fig = plt.figure(figsize=(8, 6))
    fig.tight_layout()
    for i in range(0, 20):
        ax = fig.add_subplot(5, 5, i + 1)
        ax.imshow(X[i].reshape((8,8)), cmap = "Greys", vmin = 0, vmax = 16)
    plt.show()

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
    return accuracies

def parallel_pool_tuning(cpu_count, kfolds, X, y):
    '''uses parallel cpus to cross validate best hyperplane'''
    tuning_params = np.logspace(-6, -1, 10)                                 
    partitions = np.array_split(np.random.permutation([i for i in range(0, X.shape[0])]), kfolds)
    pool = mp.Pool(cpu_count)
    args = [(X, y, tuning_params, partitions, k) for k in range(0, kfolds)] # loops for each of 5 kfolds 
    Accuracies = np.array(pool.starmap(cvkfold, args))
    pool.close()
    CV_accuracy = np.mean(Accuracies, axis = 0)                             
    best_tuning_param = tuning_params[np.argmax(CV_accuracy)]               
    return best_tuning_param

if __name__ == "__main__":
    test = np.loadtxt("optdigits.txt", delimiter = ",")
    X = test[:, 0:64]                                                       
    y = test[:, 64]                                                         
    cpu_count = 1
    kfolds = 5
    t1 = time()                                                             
    best_tuning_param = parallel_pool_tuning(cpu_count, kfolds, X, y)
    print('Best tuning param %0.5f.'% best_tuning_param)
    print('Serial runs in %0.3f seconds.' % (time() - t1))                  
    cpu_count = 2
    t2 = time()                                                             
    best_tuning_param_2 = parallel_pool_tuning(cpu_count, kfolds, X, y)
    print('Best tuning param %0.5f.'% best_tuning_param_2)
    print('2 CPU Pool runs in %0.3f seconds.' % (time() - t2))              
    cpu_count = 4
    t4 = time()                                                             
    best_tuning_param_4 = parallel_pool_tuning(cpu_count, kfolds, X, y)
    print('Best tuning param %0.5f.'% best_tuning_param_4)
    print('4 CPU Pool runs in %0.3f seconds.' % (time() - t4))              
    cpu_count = 8
    t8 = time()                                                             
    best_tuning_param_8 = parallel_pool_tuning(cpu_count, kfolds, X, y)
    print('Best tuning param %0.5f.'% best_tuning_param_8)
    print('8 CPU Pool runs in %0.3f seconds.' % (time() - t8))              