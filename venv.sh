#!/usr/bin/env fish

if not type -q conda
    echo "Conda not found. Please install Conda to use this script."
    echo "You can find installation instructions at:: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
end

set -l venv_dir "./.venv"

echo "Creating a Conda environment in the directory: $venv_dir"

conda create -p "$venv_dir" python -c conda-forge

if test $status -eq 0
    echo "The Conda environment has been successfully created."
    echo "Activating the environment..."

    conda activate "$venv_dir"
    echo "The environment has been activated."
    uv pip install -r requirements.txt
else
    echo "An error occurred while creating the Conda environment."
    exit 1
end
