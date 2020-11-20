#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=mpi_hello //name
#SBATCH --output=mpi_hello.output
#SBATCH --error=mpi_hello.err
#SBATCH --nodes=1
#SBATCH --partition express

#SBATCH --time=05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work

module load openmpi
mpicc -o mpi_hello mpi_hello.c
mpirun --mca btl_base_warn_component_unused 0 -np 4 --oversubscribe mpi_hello



