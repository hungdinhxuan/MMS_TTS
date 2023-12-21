#!/bin/bash

# Clone vits repo
git clone https://github.com/jaywalnut310/vits.git

# Clone uroman repo 
git clone git@github.com:isi-nlp/uroman.git

# Print python version
python --version

# Change to vits directory
cd vits/

# Install dependencies
pip install Cython==0.29.21
pip install librosa==0.8.0
pip install phonemizer==2.2.1 
pip install scipy
pip install numpy==1.20.0
pip install torch
pip install torchvision
pip install matplotlib 
pip install Unidecode==1.1.1
pip install numba==0.53.0

# Build monotonic align
cd monotonic_align/
mkdir monotonic_align
python3 setup.py build_ext --inplace
cd ../../

# Move inference.py to vits directory
echo "Moving inference.py to vits directory"
mv inference.py vits/
