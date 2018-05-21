#!/usr/bin/env bash

echo 'creating a conda env "soundhound_task" with dependencies for test.py...'
conda env create -f environment.yml
echo ''
echo 'activate the environment and run the file with the following commands:' 
echo 'source activate soundhound_task'
echo 'python test.py text_examples/article9000.txt'
