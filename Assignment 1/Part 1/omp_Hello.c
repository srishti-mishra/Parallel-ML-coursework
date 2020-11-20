#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc,  char *argv[])
{
int nthreads, tid;
 /* Fork a team of threads giving them their own copy of variables */
 #pragma omp parallel private (nthreads, tid)
 {
	 /* Obtain the number of thread */
  tid = omp_get_thread_num();
  printf("Hello world from thread = %d \n", tid);
  
  /* Only Master thread does this */
     if (tid == 0)
    {
	  nthreads = omp_get_num_threads();
	  printf("Total Number of threads = %d \n", nthreads);
    }
 } /* All threads join master thread and disband */
 
} 
  
	 