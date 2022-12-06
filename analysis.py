#!/usr/bin/env python3
"""Duplicate Backtrace in Crash Dump Analysis

This script allows the user to automate the process of removing duplicate crashes 
found in AFL to more carefully analyze ones that produced different outcomes. 

This tool accepts a folder of files generated by a fuzzer.

This script requires that the following libraries be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""

import os
import hashlib
import subprocess
from pygdbmi.gdbcontroller import GdbController
import argparse
from pathlib import Path
import shutil
import json

parser = argparse.ArgumentParser(
    description='Check for identical crash dumps.'
)
parser.add_argument(
    '-p', 
    '--path', 
    action='store', 
    # default='crashes', 
    help='Find where crash dump files are.',
    required=True
)
parser.add_argument(
    '-t', 
    '--target_prog', 
    action='store', 
    # default='pngslap', 
    help='Target binary to produce crashes.', 
    required=True
)
parser.add_argument(
    "-m",
    "--move",
    action="store_true",
    default=False,
    required=False
)
args = parser.parse_args()
    
def bt_with_gdb(files, path):
    """Gets a backtrace provided by GDB.

    Keyword arguments:
    files -- list of files produced by fuzzer
    path -- the target program GDB will run it against

    Returns:
    list -- an array of the path to the created backtrace files
    """
    newFileNames = []
    if os.path.exists(f"analysis_{path}"):
        shutil.rmtree(f"analysis_{path}")
    os.mkdir(f"analysis_{path}")
    for i in range(len(files)):
        if "README" not in files[i]: 
            # Create a log file containing the backtrace for each file
            gdbmi = GdbController()
            gdbmi.write(f'-file-exec-file {args.target_prog}')
            gdbmi.write(f'set logging file analysis_{path}/gdb_{files[i]}.txt')
            gdbmi.write('set logging on')
            gdbmi.write(f'set args {path}/{files[i]}')
            fileName = f"analysis_{path}/gdb_{files[i]}.txt"
            gdbmi.write('run')
            gdbmi.write('bt')
            gdbmi.exit()
            newFileNames.append(fileName)
    return newFileNames

def convert_to_hash(hash_list, list_of_files):
    """Converts a list of files to their hash representation.

    Keyword arguments:
    hash_list -- variable to populate file names to their hash
    list_of_files -- list of paths of crashes produced by fuzzer
    """
    for i in range(len(list_of_files)):
        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(list_of_files[i],'rb') as file:
        # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)
            hash_list.append([list_of_files[i], h.hexdigest()])

def sanitize(filename):
    """Sanitizes the GDB log file to just include the backtrace.

    Keyword arguments:
    filename -- name of the log file generated by the backtrace
    """
    f = open(filename, 'r')
    s = f.readlines()
    f.close()
    f = open(filename, 'w')
    # Remove contents from log file that is not the backtrace
    while '&"bt\\n"' not in s[0]:
        s.pop(0)
    while '^done' not in s[0]:
        f.writelines(s.pop(0))
    f.close()

def compare_hashes(list_of_files):
    """Compares the hashes to check for similarities.

    Keyword arguments:
    list_of_files -- list of paths of crashes produced by fuzzer

    Returns:
    list -- list of files considered non-unique
    """
    hash_list = []
    same_files = []
    origional_files = []
    no_files_found = True

    for file in list_of_files:
        sanitize(file)
    
    # convert files to hashes
    convert_to_hash(hash_list, list_of_files)
    
    # Compare the hashes of each file to determine equality
    for hash in range(len(hash_list) - 1):
        if hash_list[hash][0] not in same_files:
            for remaining_hash in range(hash + 1, len(hash_list)):
                if hash_list[remaining_hash][0] not in same_files:
                    if hash_list[hash][1] == hash_list[remaining_hash][1]:
                        if hash_list[hash][0] not in origional_files:
                            origional_files.append(hash_list[hash][0])
                            no_files_found = False
                        same_files.append(hash_list[remaining_hash][0])
            if no_files_found:
                origional_files.append(hash_list[hash][0])
        no_files_found = True

    # Print results of the comparisons
    print(f"Hashing has determined that {len(origional_files)} were unique out of {len(list_of_files)}")
    for origional_file in origional_files:
        origional_file = origional_file[origional_file.find('gdb')+1 :]
        origional_file = origional_file.replace(".txt", "")
    print(json.dumps(origional_files) + "\n")
    for same_file in same_files:
        same_file = same_file[same_file.find('gdb')+1 :]
        same_file = same_file.replace(".txt", "")
    return same_files

def get_crash_string(path):
    """Find the line in the backtrace that is believed to be the crash line.

    Keyword arguments:
    path -- the backtrace file
    """
    btFlag = False
    crashStr = ""
    # Read all lines from the file
    file = open(path, 'r')
    linesList = file.readlines()

    # Identify the line that contains the crash
    for i in range(len(linesList)-1):
        if len(linesList[i]) == len(linesList[i+1]) and btFlag:
            crashStr = linesList[i]
            startIdx = crashStr.find('0x')
            crashStr = crashStr[startIdx:]
            break
        if linesList[i].find('&"bt') == 0:
            btFlag = True
    # Return the sting of the crash
    file.close()
    return crashStr

def compareCrashes(files):
    """Compares crashes based on anticipated crash string from backtrace.
    
    Keyword arguments:
    files -- list of backtrace files
    """
    crashStrList = []
    duplicateStr = []
    duplicateFiles = []
    uniqueFileIdx = []
    uniqueFiles = []
    
    for file in files:
        crashStrList.append([file, get_crash_string(f'{file}')])

    # Compare the crash strings of each crash found
    for i in range(len(crashStrList)):
        if i not in duplicateStr:
            for j in range(len(crashStrList)):
                if j != i:
                    if j not in duplicateStr:
                        if crashStrList[i][1] == crashStrList[j][1]:
                            duplicateStr.append(j)
                            duplicateFiles.append(crashStrList[j][0])

    # Identify unique files
    for i in range(len(crashStrList)):
        if i not in duplicateStr:
            uniqueFileIdx.append(i)

    for num in uniqueFileIdx:
        uniqueFiles.append(files[num][:len(files[num])-4])

    # Print results from the comparisons
    print(f"Analysis of the backtrace has determined that {len(uniqueFileIdx)} were unique out of {len(crashStrList)}")
    for uniqueFile in uniqueFiles:
        uniqueFile = uniqueFile[uniqueFile.find('gdb')+1 :]
        uniqueFile = uniqueFile.replace(".txt", "")
    print(json.dumps(uniqueFiles) + "\n")
    for duplicateFile in duplicateFiles:
        duplicateFile = duplicateFile[duplicateFile.find('gdb')+1 :]
        duplicateFile = duplicateFile.replace(".txt", "")
    return duplicateFiles

def preform_analysis(crash_same_files, hash_same_files):
    """Do a variety of comparisons on the backtrace to determine uniqueness.

    Keyword arguments:
    crash_same_files -- crashes found to be duplicates via crash string
    hash_same_files -- crashes found to be duplicates via file hashing
    """
    crash_dup_in_both = set(crash_same_files) & set(hash_same_files)
    indetermined_same_crash = set(crash_same_files) - set(hash_same_files) - set(crash_dup_in_both)
    print(f"The following {len(crash_dup_in_both)} has been determined to be the same crash and will be moved to a new folder: {crash_dup_in_both}")
    print(json.dumps(list(crash_dup_in_both)) + "\n")
    # Create new folder for duplicate crashes
    if args.move:
        if os.path.exists("same_crash"):
            shutil.rmtree("same_crash")
        os.mkdir("same_crash")
        for file in crash_dup_in_both:
            Path(f"{Path.cwd()}/{args.path}/{file[file.find('id:'):].replace('.txt', '')}").rename(f"{Path.cwd()}/same_crash/{file[file.find('id:'):].replace('.txt', '')}")

    print(f"The following {len(indetermined_same_crash)} has been determined to could be the same crash and will be moved to a new folder:")
    print(json.dumps(list(indetermined_same_crash)) + "\n")
    # Create new folder for potential duplicate crashes
    if args.move:
        if os.path.exists("potential_duplicate"):
            shutil.rmtree("potential_duplicate")
        os.mkdir("potential_duplicate")
        for file in indetermined_same_crash:
            Path(f"{Path.cwd()}/{args.path}/{file[file.find('id:'):].replace('.txt', '')}").rename(f"{Path.cwd()}/potential_duplicate/{file[file.find('id:'):].replace('.txt', '')}")


    print(f"Backtrace files can be found in a new folder for further investigation.")


def do_comparisons(files):
    """Do a variety of comparisons on the backtrace to determine uniqueness.

    Keyword arguments:
    files -- list of backtrace files
    """
    crash_same_files = compareCrashes(files)
    hash_same_files = compare_hashes(files)
    
    preform_analysis(crash_same_files, hash_same_files)
    
def get_crash_files():
    """Gets the crash files generated by backtrace."""
    path = args.path
    files = os.listdir(path)
    files_for_analysis = bt_with_gdb(files, path)
    do_comparisons(files_for_analysis)

def main():
    get_crash_files()

if __name__ == "__main__":
    main()
