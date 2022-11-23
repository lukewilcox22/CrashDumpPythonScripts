#!/usr/bin/env python3
"""
Module Docstring
"""
import os
import hashlib
import subprocess
# import gdb
from pygdbmi.gdbcontroller import GdbController

def remove_same_crash(file):
    os.remove(file)
    pass
    
def bt_with_gdb(files):
    newFileNames = []
    for i in range(len(files)):
        gdbmi = GdbController()
        gdbmi.write(f'-file-exec-file pngslap')
        gdbmi.write(f'set logging file {files[i]}.txt')
        gdbmi.write('set logging on')
        gdbmi.write(f'set args crashes_qsymgenerated_nov10/{files[i]}')
        fileName = f"{files[i]}.txt"
        response = gdbmi.write('run')
        print(response)
        gdbmi.write('bt')
        gdbmi.exit()
        newFileNames.append(fileName)
    return newFileNames

"""def convert_to_hash(same_files, list_of_files):
    for i in range(len(list_of_files)):
        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(filename,'rb') as file:

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
    
    convert_to_hash(same_files, list_of_files)
        
    for hash in range(len(hash_list)) - 1:
        for compare_hash + 1 in range(len(hash_list)):
            if compare_hash[0] not in same_files:
                if hash[1] is compare_hash[1]:
                    if hash[0] not in same_files:
                        same_files.append(hash[0])
                    same_files.append(compare_hash[1]
        
    return same_files
"""  

def do_comparisons(files):
    newFiles = bt_with_gdb(files)
    print(newFiles)
    # Can do string by string comparison
    # Compare hash of the bytestream from a file
    # Ambitious: Compare stack frames of the crashes
    # Find more ways to analyze crash dumps and then somehow compare them
    pass

def get_crash_files():
    path = "/home/matthewyfong/CSE_5472/CrashDumpPythonScripts/crashes_qsymgenerated_nov10"
    files = os.listdir(path)
    print(files)
    #compare_hashes(files)
    do_comparisons(files)
    pass

def compareToAll(all, string):
    """Compares string to all strings in all
    @all    :Array of list
    @string :String"""
    for i in range(len(all)):
        if string == all[i]:
            print(f'String is similar to string at {i}')
        else:
            print("Strings are not similar")

def compareStringsInCrashdumps():
    """Compare strings in the crash dump file--- To be changed"""
    """Use back traces to check similarities between crash dumps"""
    output = []
    for i in range(10):
        file = f"id00{i}strings"
        bashCommand = ["touch", file]
        bashCommand = ["strings", f"id00{i}"]
        process = subprocess.run(bashCommand, capture_output=True)
        output.append(str(process.stdout))

    for i in range(len(output)):
        print(f"Comparing all strings to {i}")
        compareToAll(output, output[i])


def main():
    get_crash_files()


if __name__ == "__main__":
    main()
