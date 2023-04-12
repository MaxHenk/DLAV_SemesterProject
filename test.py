#!/bin/bash
#SBATCH --chdir=/scratch/bpoffet/DLAV_SemesterProject/test.py
#SBATCH --nodes 1
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 8G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --qos
#SBATCH --account civil-459
#SBATCH --reservation dlav

print("hello from bpoffet")

