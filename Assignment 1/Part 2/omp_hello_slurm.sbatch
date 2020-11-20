#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=omp_hello //name
#SBATCH --output=omp_hello.output
#SBATCH --error=omp_hello.err

#SBATCH --partition express
#SBATCH --nodes=1
#SBATCH --time=0:05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work
module load gcc
gcc -o omp_hello -fopenmp omp_Hello.c
export OMP_NUM_THREADS=8
./omp_hello
