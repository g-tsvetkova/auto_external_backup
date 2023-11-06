#! python3
# autobackup.py

import dirsync
import os
from utils import estimate_backup_size, visualize_backup_statistics

src = "Path_To_Folder_Being_Backedup"
dest = "Path_To_External_Drive"

if os.path.exists(dest):
    # Calculate the estimated backup size
    estimated_size = estimate_backup_size(src)
    print(f"Estimated backup size: {estimated_size} bytes")

    # Synchronize the directories
    dirsync.sync(src, dest, 'sync', purge=True)

    # Visualize backup statistics
    visualize_backup_statistics(src, dest)
else:
    print("Backup storage not found. Exiting...")
