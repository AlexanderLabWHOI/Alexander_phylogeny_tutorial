#!/usr/bin/bash
#SBATCH --time=23:59:59
#SBATCH --partition=scavenger,compute,medmem
#SBATCH --mem=128gb
#SBATCH --cpus-per-task=8
#SBATCH --job-name=clustal
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

eval "$(conda shell.bash hook)"

conda activate phylogeny
 clustalo -i all_amts.fa -o all_amts_clustal.fa.fas --threads=16 --force
