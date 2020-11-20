#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=omp //name
#SBATCH --output = omp.output
#SBATCH --error = omp.err
#SBATCH --partition=express
#
# Time format = HH:MM:SS, DD-HH:MM:SS
#SBATCH --time=05:00
#SBATCH -N 1

work=$HOME/csye7374-mishra.sr/homework1
cd $work

module load gcc

gcc -o mm_omp -fopenmp mm_omp.c

export OMP_NUM_THREADS=2
./mm_omp
export OMP_NUM_THREADS=4
./mm_omp
export OMP_NUM_THREADS=8
./mm_omp






