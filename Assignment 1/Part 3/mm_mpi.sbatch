#!/bin/bash

##Normal configurations

##slurm script
#SBATCH --job-name=mpi //name
#SBATCH --output=mpi.output
#SBATCH --error=mpi.err
#SBATCH --time=0-00:05:00 //time for 5 mins

## Parallel Configurations
#SBATCH --partition express
#SBATCH -N 1



work=$HOME/csye7374-mishra.sr/homework1
cd $work

module load openmpi

mpicc -o mm_mpi mm_mpi_.c

echo " With Core 2"
echo "---------------------------------------------------------------------------------"
mpirun --mca btl_base_warn_component_unused 0 -np 2 --oversubscribe mm_mpi
echo " With Core 4"
echo "---------------------------------------------------------------------------------"
mpirun --mca btl_base_warn_component_unused 0 -np 4 --oversubscribe mm_mpi
echo "With Core 8"
echo "---------------------------------------------------------------------------------"
mpirun --mca btl_base_warn_component_unused 0 -np 8 --oversubscribe mm_mpi