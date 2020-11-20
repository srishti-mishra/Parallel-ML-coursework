# include "mpi.h"
# include <stdio.h>
#define SIZE 4

main (int argc, char *argv[])
{
	int numtasks, rank, sendcount, recvcount, source;
	float sendbuf [SIZE][SIZE] ={
		{1.0, 2.0,3.0,4.0},
		{5.0, 6.0,7.0,8.0},
		{9.0, 10.0,11.0,12.0},
	    {13.0, 14.0,15.0,16.0} };
		
	float recvbuff [SIZE];

    MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
	 MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	 
	 if(numtasks = SIZE){
		 //define source task and elements to send/receive then perform collective scatter
		 source =1;
		 sendcount = SIZE;
		 recvcount = SIZE;
		 MPI_Scatter(sendbuf, sendcount, MPI_FLOAT, recvbuff, recvcount,
		 MPI_FLOAT, source, MPI_COMM_WORLD);
		 
		 printf("rank = %d Results: %f %f %f %f \n",rank, recvbuff[0], recvbuff[1], recvbuff[2], recvbuff[3]);
	 }
	 else
		 printf ("Must specify %d processors. Termintating. \n" , SIZE);
	 
	 MPI_Finalize();
}