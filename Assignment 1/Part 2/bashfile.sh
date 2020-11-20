#!/bin/bash

##sbatch of all the 5 files

sbatch mpi_hello_slurm.sbatch
sbatch mpi_scatter_slurm.sbatch
sbatch omp_hello_slurm.sbatch
sbatch omp_loop_slurm.sbatch
sbatch omp_func_slurm.sbatch

