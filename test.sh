#!/bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --begin=now
#SBATCH --mem 40G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --qos dlav
#SBATCH --reservation civil-459
#SBATCH --account civil-459-2023

python3 test.py

echo "It worked!"
