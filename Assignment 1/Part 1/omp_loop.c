#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
# define N   100

int main (int argc, char *argv[])
{
int nthreads, i, tid;
float a[N], b[N], c[N];

/* Some initialization */
for (i=0; i<N; i++)
	a[i] = b[i] = i;

# pragma omp parallel shared (a,b,c, nthreads) private (i, tid)
 {
	tid = omp_get_thread_num();
	if (tid ==0)
	 {
		nthreads = omp_get_num_threads();
		printf("Total number of threads = %d \n", nthreads);
	 }
	printf("Thread %d starting.... \n", tid);
	
	#pragma omp for 
	for(i=0; i<N; i++)
	 {
		c[i] = a[i] + b[i];
		printf("Thread %d : c[%d] =  %f \n", tid, i, c[i]);
	 }
 } /* end of parallel section */
}