#!/bin/bash

# Set the source and destination paths
src="/Users/backup"
dest="/Volumes/Untitled/sda1"

# Check if the external drive is mounted
if [ -d "$dest" ]; then
    # Run the Python script
    python3 autobackup.py
else
    echo "Backup storage not found. Exiting..."
fi
