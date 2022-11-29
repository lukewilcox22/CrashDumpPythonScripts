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

parser = argparse.ArgumentParser(
    description='Check for identical crash dumps.'
)
parser.add_argument(
    '--path', 
    action='store', 
    # default='crashes_qsymgenerated_nov10', 
    help='Find where crash dump files are.',
    required=True
)
parser.add_argument(
    '--target_prog', 
    action='store', 
    # default='pngslap', 
    help='Target binary to produce crashes.', 
    required=True
)
# parser.add_argument('--target_prog', action='store', help='Target program for AFL to run.', required=True)
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
    os.mkdir(f"analysis_{path}")
    for i in range(len(files)):
        if "README" not in files[i]: 
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

    for file in files_for_analysis:
        sanitize(file)
    
    convert_to_hash(hash_list, list_of_files)
        
    for hash in range(len(hash_list) - 1):
        if hash_list[hash][0] not in same_files:
            for remaining_hash in range(hash + 1, len(hash_list)):
                if hash_list[remaining_hash][0] not in same_files:
                    print(f"{hash_list[hash][1]} and {hash_list[remaining_hash][1]}")
                    if hash_list[hash][1] == hash_list[remaining_hash][1]:
                        if hash_list[hash][0] not in origional_files:
                            origional_files.append(hash_list[hash][0])
                        same_files.append(hash_list[remaining_hash][0])
    print(f"Hashing has determined that {len(origional_files)} were unique out of {len(list_of_files)}")
    return same_files

def get_crash_string(path):
    """Find the line in the backtrace that is believed to be the crash line.

    Keyword arguments:
    path -- the backtrace file
    """
    btFlag = False
    file = open(path, 'r')
    linesList = file.readlines()
    for i in range(len(linesList)):
        if len(linesList[i+1]) == len(linesList[i+2]) and btFlag:
            crashStr = linesList[i]
            startIdx = crashStr.find('0x')
            crashStr = crashStr[startIdx:]
            break
        if linesList[i].find('&"bt') == 0:
            btFlag = True
    file.close()
    return crashStr

def compareCrashes():
    """Compares crashes based on anticipated crash string from backtrace."""
    crashStrList = []
    duplicateStr = []
    duplicateFiles = []
    files = os.listdir(args.path)
    for file in files:
        crashStrList.append(get_crash_string(f'{args.path}/{file}'))
    for i in range(len(crashStrList)):
        if i not in duplicateStr:
            for j in range(len(crashStrList)):
                if j != i:
                    if j not in duplicateStr:
                        if crashStrList[i] == crashStrList[j]:
                            duplicateStr.append(j)

    for num in duplicateStr:
        duplicateFiles.append(files[num][:len(files[num])-4])
    print(f"Analysis of the backtrace has determined that {len(crashStrList)} were unique out of {len(crashStrList)}")
    return duplicateFiles

def preform_analysis(crash_same_files, hash_same_files):
    """Do a variety of comparisons on the backtrace to determine uniqueness.

    Keyword arguments:
    crash_same_files -- crashes found to be duplicates via crash string
    hash_same_files -- crashes found to be duplicates via file hashing
    """
    crash_dup_in_both = list(set(crash_same_files) & set(hash_same_files))
    indetermined_same_crash = list(set(crash_same_files) - set(hash_same_files))
    print(f"The following has been determined to be the same crash and will be moved to a new folder: {crash_dup_in_both}")
    os.mkdir("same_crash")
    for file in crash_dup_in_both:
        os.replace(file, f"same_crash/{file}")

    print(f"The following has been determined to can be the same crash and will be moved to a new folder: {indetermined_same_crash}")
    os.mkdir("potential_duplicate")
    for file in indetermined_same_crash:
        os.replace(file, f"potential_duplicate/{file}")

    print(f"Backtrace files can be found in a new folder for further investigation.")


def do_comparisons(files):
    """Do a variety of comparisons on the backtrace to determine uniqueness.

    Keyword arguments:
    files -- list of backtrace files
    """
    crash_same_files = compareCrashes()
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
