#!/bin/bash
#SBATCH --job-name=infer-text
#SBATCH --output=result.out
#SBATCH --error=result.err
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --mem=2G

module load python/3.10 

python inference_script.py "The protagonist faced internal conflict."
