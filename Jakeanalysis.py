#!/usr/bin/env python3
"""
Module Docstring
"""
import os

def remove_same_crash(file):
    os.remove(file)
    pass
    
def bt_with_gdb(files):
    for i in files:
	    os.system('gdb')
	    os.system('set logging on')
	    os.system('set logging file ' + files[i] + '.log')
	    os.system('quit')
	    os.system('y')
	    fileName = 'gdb ' + files[i]
	    os.system(fileName)
	    os.system('run')
	    os.system('bt')
	    os.system('quit')
	    os.system('y')
    
def convert_to_hash(same_files, list_of_files):
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
    

def do_comparisons():
    bt_with_gdb()
    # Can do string by string comparison
    # Compare hash of the bytestream from a file
    # Ambitious: Compare stack frames of the crashes
    # Find more ways to analyze crash dumps and then somehow compare them
    pass

def get_crash_files():
    path = "/home/vagrant/qsym/outside_tests/crashes"
    files = os.listdir(path)
    compare_hashes(files)
    bt_with_gdb(files)
    pass

def main():
    pass


if __name__ == "__main__":
    main()
