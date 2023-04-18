#!/bin/bash
#SBATCH --chdir=/scratch/bpoffet/DLAV_SemesterProject
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --mem 40G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --account civil-459-2023
#SBATCH --reservation civil-459-2023


print("hello from bpoffet")

