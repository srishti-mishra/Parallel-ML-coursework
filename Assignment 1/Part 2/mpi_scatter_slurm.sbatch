#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=mpi_scatter //name
#SBATCH --output=mpi_scatter.output
#SBATCH --error=mpi_scatter.err
#SBATCH --partition express
#SBATCH --nodes=1
#SBATCH --time=0:05:00

work=$HOME/csye7374-mishra.sr/homework1
cd $work

module load openmpi
mpicc -o mpi_scatter mpi_scatter_.c
mpirun --mca btl_base_warn_component_unused 0 -np 4 --oversubscribe mpi_scatter




