#!/usr/bin/env python3
"""
Module Docstring
"""
import os
import hashlib
import subprocess
from pygdbmi.gdbcontroller import GdbController
import argparse

parser = argparse.ArgumentParser(description='Check for identical crash dumps.')
parser.add_argument('--path', action='store', default='crashes_qsymgenerated_nov10', help='Find where crash dump files are.', required=False)
parser.add_argument('--target_prog', action='store', default='pngslap', help='Target program for AFL to run.', required=False)
# parser.add_argument('--target_prog', action='store', help='Target program for AFL to run.', required=True)
args = parser.parse_args()

def remove_same_crash(file):
    os.remove(file)
    pass
    
def bt_with_gdb(files, path):
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

def compare_hashes(list_of_files):
    hash_list = []
    same_files = []
    origional_files = []
    
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
    print(origional_files)
    return same_files
 

def do_comparisons(files):
    # Can do string by string comparison
    same_files = compare_hashes(files)
    print(same_files)
    # Ambitious: Compare stack frames of the crashes
    # Find more ways to analyze crash dumps and then somehow compare them

def get_crash_string(path):
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
    crashStrList = []
    duplicateStr = []
    duplicateFiles = []
    path = "/home/luke/CrashDumpPythonScripts/bt_nov10"
    files = os.listdir(path)
    for file in files:
        crashStrList.append(get_crash_string(f'/home/luke/CrashDumpPythonScripts/bt_nov10/{file}'))
    for i in range(len(crashStrList)):
        if i not in duplicateStr:
            for j in range(len(crashStrList)):
                if j != i:
                    if j not in duplicateStr:
                        if crashStrList[i] == crashStrList[j]:
                            duplicateStr.append(j)

    for num in duplicateStr:
        duplicateFiles.append(files[num][:len(files[num])-4])
    return duplicateFiles

def sanitize(filename):
    """Sanitize dump file"""
    f = open(filename, 'r')
    s = f.readlines()
    f.close()
    f = open(filename, 'w')
    while '&"bt\\n"' not in s[0]:
        s.pop(0)
    while '^done' not in s[0]:
        f.writelines(s.pop(0))
    f.close()

def do_comparisons(files):
    # Can do string by string comparison
    same_files = compare_hashes(files)
    print(same_files)
    # Ambitious: Compare stack frames of the crashes
    # Find more ways to analyze crash dumps and then somehow compare them
    
def get_crash_files():
    path = args.path
    files = os.listdir(path)
    files_for_analysis = bt_with_gdb(files, path)
    for file in files_for_analysis:
        sanitize(file)
    do_comparisons(files_for_analysis)

def main():
    get_crash_files()


if __name__ == "__main__":
    main()
