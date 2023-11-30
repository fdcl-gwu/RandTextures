#!/bin/bash

#SBATCH --job-name=MuWiH
#SBATCH -o logs/JobID_%j_nodeID_%n.out
#SBATCH -e logs/JobID_%j_nodeID_%n.err 
#SBATCH --nodes=1
# SBATCH --ntasks=4
# SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=30
#SBATCH --mem-per-cpu=10000
#SBATCH -p small-gpu
#SBATCH -t 7-00:00:00 

python3 GenRandom.py