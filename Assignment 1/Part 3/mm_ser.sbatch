#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=mpi //name
#SBATCH --output=mpi.output
#SBATCH --error=mpi.err

## Parallel Configurations

#SBATCH --nodes 1
#SBATCH --partition express
#SBATCH --time=05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work
module load gcc

gcc -o mm_ser -fopenmp mm_serial.c
./mm_ser




