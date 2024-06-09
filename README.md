# Veeam Folder Synchronization Task

This repository contains the necessary files and instructions for the program to successfully synchronize files from a `source` to a `replica` folder. The program guarantees that the `replica` folder is an exact copy of the `source` folder by calculating the MD5 hashes using Python's `hashlib`<a href="#">[1]</a> library to ensure file integrity. This project is implemented in Python on a Debian 12 system.


The operations are logged to both a log file and the terminal, including all file operations such as creation, copying, and removal. Additionally, the synchronization interval can be manually specified in seconds.


## Principal adventajes

- **One-way and accurate synchronization**: The program synchronizes the folder source's contents exactly and identically to the folder replica using the MD5 hash calculations for verification.

- **Periodic Synchronization**: Runs at a specified interval defined by the user.

- **Logging**: This option logs file operations like copying, creating, and removing files to the console and a defined log file.

- **Cross-Platform**: Because Python and its libraries are flexible, the program must work on any system where Python is installed.


## To Do list:

- **Optional GUI**: Optional argument which will include a graphical user interface using PyQt 
- **Notifications**: Different types of users and purposes would be able to receive notifications, for example, via email using `email.message` or by telegram with a bot. 


## How to install and use

1. Clone the repository:
    ```bash
    git clone https://github.com/maurcabezas/synch_task.git
    cd synch_task
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Using:

    ### Command-Line 
    Run the script from the command line:
    ```bash
    python FolderSync.py <source_folder_path> <replica_folder_path> <sync_interval_seconds> <log_file_path>
