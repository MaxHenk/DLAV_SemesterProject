#!/bin/bash
#SBATCH --chdir /scratch/<put-your-username-here>
#SBATCH --nodes 1
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 1G
#SBATCH --account scitas-courses
#SBATCH --reservation intro2clusters
sleep 10
echo "hello from $(hostname)"
sleep 10
