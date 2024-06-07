# Veeam Folder Synchronization Task

This repository contains the necessary files and instructions to successfully synchronize files from a `source` folder to a `replica` folder. The program ensures that the `replica` folder is an exact copy of the `source` folder, including all file operations such as creation, copying, and removal. The operations are logged to both a log file and the terminal. Additionally, the synchronization interval can be manually specified in seconds.

The program calculates MD5 hashes using Python's `hashlib` library to ensure file integrity. This project is implemented in Python on a Debian 12 system.


## Main Features

- **One-way Synchronization**: From source to replica.
- **Periodic Synchronization**: Runs at a specified interval.
- **Logging**: Logs file operations to the console and a log file.
- **Optional GUI**: Includes a graphical user interface using PyQt.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/maurcabezas/synch_task.git
    cd synch_task
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command-Line 
Run the script from the command line:
```bash
python FolderSync.py <source_folder_path> <replica_folder_path> <sync_interval_seconds> <log_file_path>
```


