#!/bin/sh
#SBATCH -o outfile3  # send stdout to outfile
#SBATCH -e errfile3  # send stderr to errfile
#SBATCH -t 1-05:00:00  # time requested in hour:minute:second
#SBATCH -p barbun-cuda
#SBATCH -c 40
#SBATCH --gres=gpu:2

echo "date" `date`

cd /truba/home/mkutlu/bahadir/bert-sample
python train_sample.py
