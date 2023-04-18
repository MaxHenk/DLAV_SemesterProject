#!/bin/bash
#SBATCH --chdir=/home/bpoffet/DLAV_SemesterProject
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --begin=now
#SBATCH --mem 40G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --account civil-459-2023

echo "It worked!" >> output_file

