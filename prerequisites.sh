#!/bin/bash

# Check if cmake is installed
if ! command -v cmake &> /dev/null
then
    echo "cmake not found. Installing..."
    # For Ubuntu/Debian
    sudo apt-get update
    sudo apt-get install -y cmake python3-tk
else
    echo "cmake is already installed."
fi

# Install the required Python packages
pip install -r requirements.txt
