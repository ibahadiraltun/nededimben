#!/bin/sh
#SBATCH -o outfile  # send stdout to outfile
#SBATCH -e errfile  # send stderr to errfile
#SBATCH -t 0-01:00:00  # time requested in hour:minute:second
#SBATCH -p akya-cude

echo "date" `date`

cd /truba/home/mkutlu/bahadir/bert-sample
python train_sample.py
