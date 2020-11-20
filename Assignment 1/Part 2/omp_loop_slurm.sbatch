#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=omp_loop //name
#SBATCH --output=omp_loop.output
#SBATCH --error=omp_loop.err
#SBATCH --nodes=1
#SBATCH --partition express

#SBATCH --time=05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work
module load gcc

gcc -o omp_loop -fopenmp omp_loop.c
export OMP_NUM_THREADS=8
./omp_loop

