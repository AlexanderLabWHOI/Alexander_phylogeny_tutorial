#!/usr/bin/bash
#SBATCH --time=23:59:59
#SBATCH --partition=medmem,scavenger,compute
#SBATCH --mem=128gb
#SBATCH --job-name=iqtree
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

eval "$(conda shell.bash hook)"
conda activate phylogeny
 iqtree -s all_amts_muscle_curated.fa.fas -bb 1000 -alrt 1000 -m TEST -redo
