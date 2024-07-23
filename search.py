# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:48:41 2024

@author: Corrina Alcoser
github: core-creates
library: file_search 
info: recursively search through all directories on all drives on the system

"""
import os
import time, stat

def get_drives():
    """
    Get a list of available drives.

    Returns:
    list: A list of available drives.
    """
    drives = [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]
    print("Available drives:", drives)
    return drives

def list_directories(startpath):
    """
    Recursively lists all directories starting from the given path.

    Parameters:
    startpath (str): The root directory to start the search from.

    Returns:
    None
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for d in dirs:
            print(f"{subindent}{d}")
            #return f"{subindent}{d}"

def list_files(drives):
    """
    Recursively lists all files and directories on the given drives.

    Parameters:
    drives (list): A list of drive letters to search.

    Returns:
    None
    """
    for drive in drives:
        for root, dirs, files in os.walk(drive + "\\"):
            level = root.replace(drive + "\\", '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")

def find_file(drives, filename):
    """
    Recursively searches for a specific file on the given drives.

    Parameters:
    drives (list): A list of drive letters to search.
    filename (str): The name of the file to search for.

    Returns:
    None
    """
    for drive in drives:
        for root, dirs, files in os.walk(drive + "\\"):
            if filename in files:
                searched_file_path = os.path.join(root, filename)
                #print(searched_file_path)
                return searched_file_path

def last_modified_file(drives, filename):
    # Look through all drives
    for drive in drives:
        for root, dirs, files in os.walk(drive + "\\"):
            if filename in files:
                searched_file_path = os.path.join(root, filename)
                print(searched_file_path)
                # current time - last modified time
                dtime = time.time() - os.stat(searched_file_path)[stat.ST_MTIME]
                if dtime <= 30:   # 30 seconds
                    print("Found modification within last 30 seconds.")
                    return dtime
                else:
                    print(f'Last Modification was {dtime:,} seconds ago')
                    return dtime
