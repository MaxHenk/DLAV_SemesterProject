#!/bin/bash
#SBATCH --chdir /home/bpoffet/DLAV_SemesterProject
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 8G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --account civil-459
#SBATCH --reservation civil-459

print("hello from bpoffet")

