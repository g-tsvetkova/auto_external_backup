#! python3
# File: autobackup.py

import dirsync
import os

src = "Path_To_Folder_Being_Backedup"
dest = "Path_To_External_Drive"

if os.path.exists(dest):
    dirsync.sync(src, dest, 'sync', purge=True)
else:
    print("Backup storage not found. Exiting...")
