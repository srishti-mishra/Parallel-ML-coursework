#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=omp_func //name
#SBATCH --output=omp_func.output
#SBATCH --error=omp_func.err

#SBATCH --nodes=1
#SBATCH --partition express
#SBATCH --time=05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work
module load gcc

gcc -o omp_func -fopenmp omp_function.c
export OMP_NUM_THREADS=8
./omp_func


