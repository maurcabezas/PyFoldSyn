import os
import shutil
import time
import hashlib
import logging
import sys
from argparse import ArgumentParser

class FolderSync:
    """
    This class synchronize all the contents of a source directory to a replica directory,
    keeping them in exactly in sync.
    """

    def __init__(self, source, replica, interval, log_file):
        """
        Function which initialize and read the arguments
        
        List of arguments:
            source (str): Path to the source directory.
            replica (str): Path to the replica directory.
            interval (int): Interval in seconds between synchronizations.
            log_file (str): Path to the log file.
            logger (logging.Logger): Logger object for logging messages.
        """
        self.source = source
        self.replica = replica
        self.interval = interval
        self.log_file = log_file
        self.logging()
    
    def logging(self):
        """
        Configures logging for the FolderSync class.
        """
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[logging.FileHandler(self.log_file),
                                      logging.StreamHandler()])
    
    def md5_checksum(self, file_path):
        """
        Calculates the MD5 checksum of a file to verify the exact copy.
        """
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def synchronize(self):
        """
        Continuously synchronizes the source and replica directories.
        """
        while True:
            self.sync_folders()
            time.sleep(self.interval)
    
    def sync_folders(self):
        """
        Synchronizes the contents of the source and replica directories by copying or removing the contents.
        """
        self.copy_files()
        self.remove_extra_files()
    
    def copy_files(self):
        """
        Copies files from the source directory to the replica directory if they are not already on the replica folder or are updated.
        """
        for root, dirs, files in os.walk(self.source):
            relative_path = os.path.relpath(root, self.source)
            replica_path = os.path.join(self.replica, relative_path)
            

            if not os.path.exists(replica_path):
                os.makedirs(replica_path)
                logging.info(f'Created directory: {replica_path}')
            
            for file in files:
                source_file = os.path.join(root, file)
                replica_file = os.path.join(replica_path, file)
                
            #     if not os.path.exists(replica_file) or self.md5_checksum(source_file) != self.md5_checksum(replica_file):
            #         shutil.copy2(source_file, replica_file)
            #         logging.info(f'Copied/Updated file: {source_file} to {replica_file}')


            # for file in files:
            #     source_file = os.path.join(root, file)
            #     replica_file = os.path.join(replica_path, file)

                # Check for existence or outdated files in replica
                if not os.path.exists(replica_file):
                    shutil.copy2(source_file, replica_file)
                    logging.info(f"Copied file: {source_file} to {replica_file}")
                elif self.md5_checksum(source_file) != self.md5_checksum(replica_file):
                    shutil.copy2(source_file, replica_file)
                    logging.info(f"Updated file: {source_file} to {replica_file}")

                    
    
    def remove_extra_files(self):
        """
        Removes files from the replica directory if they are not present in the source directory.
        """
        for root, dirs, files in os.walk(self.replica):
            relative_path = os.path.relpath(root, self.replica)
            source_path = os.path.join(self.source, relative_path)
            
            if not os.path.exists(source_path):
                shutil.rmtree(root)
                logging.info(f'Removed directory: {root}')
                continue
            
            for file in files:
                replica_file = os.path.join(root, file)
                source_file = os.path.join(source_path, file)
                
                if not os.path.exists(source_file):
                    os.remove(replica_file)
                    logging.info(f'Removed file: {replica_file}')

def main():
    """
    Parses command-line arguments and starts the synchronization process.
    """
    parser = ArgumentParser(description="Synchronize two folders")
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("replica", help="Replica folder path")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Log file path")
    args = parser.parse_args()
    
    synchronizer = FolderSync(args.source, args.replica, args.interval, args.log_file)
    synchronizer.synchronize()

if __name__ == "__main__":
    main()
