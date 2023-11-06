# auto_external_backup

This repository contains a Python script and a shell script to automate the backup process when an external drive is plugged into your macOS computer. The script will check if the specified external drive is mounted and then sync a source folder with the external drive using dirsync.

# Prerequisites
macOS: This script is designed to work on macOS.
Python 3: Ensure that Python 3 is installed on your system.

# Getting Started
Follow these steps to set up the automated backup script:

1. Clone the Repository
```
   git clone https://github.com/yourusername/automated-backup-script.git
```
2. Customize the Backup Configuration
Edit the autobackup.py script to specify your source and destination paths. Replace the placeholders with the actual paths.
```
src = "Path_To_Folder_Being_Backedup"
dest = "Path_To_External_Drive"
```
3. Customize the Shell Script
Modify the shell script (backup.sh) to check if the external drive is mounted and execute the Python script.

5. Make the Shell Script Executable
In the terminal, navigate to the directory containing the backup.sh script and make it executable with the following command:
```
chmod +x backup.sh
```
5. Create a Launch Agent
Create a .plist file in the ~/Library/LaunchAgents directory to trigger the shell script when the external drive is mounted. Customize the .plist file with the appropriate paths:
- Replace /path/to/backup.sh with the actual path to your shell script.

6. Load the Launch Agent
To load the Launch Agent, run the following command in the Terminal:
```
launchctl load ~/Library/LaunchAgents/com.mybackup.autobackup.plist
```
7. Test the Script
Plug in your external hard drive. When it's mounted, the script backup.sh will run, which in turn runs your Python script, creating an automated backup.

# Usage
To perform a backup, simply plug in your external drive. The script will automatically run and sync your specified source folder with the external drive.

# Customization
You can further customize the backup process by modifying the Python script (autobackup.py) to suit your specific needs. You can change the synchronization method, include exclusion rules, or implement other backup strategies using the dirsync library.

# Acknowledgments
- dirsync: Python library used for directory synchronization.
- Apple Launch Services: Used for triggering scripts when specific events occur.

# Questions and Issues
If you have any questions or encounter issues with the script, please feel free to open an issue on this GitHub repository.

