# utils.py

import os
import dirsync
import matplotlib.pyplot as plt

def get_directory_size(path):
    """
    Calculate the size of a directory in bytes.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def estimate_backup_size(src):
    """
    Estimate the size of the backup based on the source directory.
    """
    src_size = get_directory_size(src)
    return src_size

def visualize_backup_statistics(src, dest):
    """
    Visualize statistics about the backup process.
    """
    src_size = estimate_backup_size(src)
    dest_size = get_directory_size(dest)

    labels = 'Source', 'Destination'
    sizes = [src_size, dest_size]
    colors = ['#ff9999', '#66b3ff']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Backup Statistics")

    plt.show()
