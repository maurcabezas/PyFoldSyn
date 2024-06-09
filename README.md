# Veeam Folder Synchronization Task

This repository contains the necessary files and instructions for the program to successfully synchronize files from a `source` to a `replica` folder. The program guarantees that the `replica` folder is an exact copy of the `source` folder by calculating the MD5 hashes using Python's `hashlib`[1] library to ensure file integrity. This project is implemented in Python on a Debian 12 system.


The operations are logged to both a log file and the terminal, including all file operations such as creation, copying, and removal. Additionally, the synchronization interval can be manually specified (in seconds).


## Principal adventajes

- **One-way and accurate synchronization**: The program synchronizes the folder source's contents exactly and identically to the folder replica using the MD5 hash calculations for verification.

- **Periodic Synchronization**: Runs at a specified interval defined by the user.

- **Logging**: This option logs file operations like copying, creating, and removing files to the console and a defined log file.

- **Cross-Platform**: Because Python and its libraries are flexible, the program must work on any system where Python is installed.


## To Do list:

- **Optional GUI**: Optional argument which will include a graphical user interface using PyQt 
- **Notifications**: Different types of users and purposes would be able to receive notifications, for example, via email using `email.message`[2] or by telegram with a bot. 


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
    ```

    ### Example
    A folder source, as example is provided in the path /test/source
    ```bash
    python FolderSync.py tests/source/ replica/ 10 log.txt
    ```
    In this example, we synchronised the test folder source periodically every 10 seconds (a short period of time is recommended for the test). In the terminal and in the file 'log.txt' we can see:

```
2024-06-10 00:40:14,159 - INFO - Created directory: replica/.
2024-06-10 00:40:14,170 - INFO - Copied/Updated file: tests/source/test_file5.html to replica/./test_file5.html
2024-06-10 00:40:14,171 - INFO - Copied/Updated file: tests/source/test_file3.json to replica/./test_file3.json
2024-06-10 00:40:14,171 - INFO - Copied/Updated file: tests/source/test_file1.txt to replica/./test_file1.txt
2024-06-10 00:40:14,171 - INFO - Copied/Updated file: tests/source/test_file4.xml to replica/./test_file4.xml
2024-06-10 00:40:14,172 - INFO - Copied/Updated file: tests/source/test_file2.csv to replica/./test_file2.csv
2024-06-10 00:41:24,253 - INFO - Copied/Updated file: tests/source/test_file1 (copy).txt to replica/./test_file1 (copy).txt
2024-06-10 00:41:44,277 - INFO - Removed file: replica/test_file1 (copy).txt
```


## References:
<a href="https://docs.python.org/3/library/hashlib.html">[1] https://docs.python.org/3/library/hashlib.html</a> 

<a href="https://docs.python.org/3/library/email.message.html">[2] https://docs.python.org/3/library/email.message.html</a>
