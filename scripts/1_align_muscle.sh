#!/usr/bin/bash
#SBATCH --time=23:59:59
#SBATCH --partition=scavenger,compute,medmem
#SBATCH --mem=128gb
#SBATCH --cpus-per-task=8
#SBATCH --job-name=muscle
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

eval "$(conda shell.bash hook)"

conda activate phylogeny
muscle -align ../sample_data/all_amts.fa -output ../sample_data/all_amts_muscle.fa.fas
