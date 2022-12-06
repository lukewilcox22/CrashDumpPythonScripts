CrashDumpPythonScripts - Compare a set of AFL/QSYM generated crash files to determine unique crashes

Running analysis.py will create a new directory that will store the sanitized log files created by GDB.
It will also move the known duplicates and potential duplicate crash files into their own respective directories, leaving the unique crashes in the original crash directory.

How to run:

    Prerequisites:
        - Prepared folder with crash files from AFL/QSYM in working directory
        - Target program that was ran to find crashes (already compiled for GDB)
        - Download and install GDB
        - Download pygdbmi using steps found in https://github.com/cs01/pygdbmi
    Running:
        - $ python3 analysis.py --path [path to crash directories] --target_prog [name of target program] -m

    The path parameter tells the program to know where the crash files are located.
    The target_prog parameter tells the program the name of the test program and where it's located.
    The m parameter is used to move the duplicate files to new directories.

Steps for QSYM Vagrant environment:

    Install Vagrant:

    - Download VagrantFile from https://app.vagrantup.com/insuyun/boxes/qsym
    - In Folder with VagrantFile run:
        - $ vagrant init
    - In VagrantFile, edit it so it includes inside of “config.vm.provider "virtualbox" do |v|”
        - vb.memory = 4096 
        - vb   .cpus = 4 
        - vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    - Start up VM:
        - $ vagrant up
    - ssh into VM:
        - $ vagrant ssh

    Run libpng in Vagrant:
    - EVERYTIME Run in home directory $ sudo sysctl --system
    - EVERYTIME Run in home directory $ sudo ldconfig
    - Get and edit Makefile in libpng directory to use afl gcc
        - In our case, we had to change CC=/home/vagrant/afl-2.52b/gcc
    - Run in libpng directory $ make
        - In our case, we’re getting scripts/makefile.linux to use
    - Run in libpng directory $ sudo make install
    - Compile target program in afl directory with $ afl-gcc -g -o example example.c -lpng -lz -lm
    - EVERYTIME Run echo core >/proc/sys/kernel/core_pattern in root
    - EVERYTIME Run AFL Master in home directory $ AFL_NO_FORKSRV=1 ./afl-2.52b/afl-fuzz -M afl-master -i input -o output -- ./our_qsym/outside_tests/pngslap @@ /dev/null
    - EVERYTIME Run AFL Slave in home directory $ ./afl-2.52b/afl-fuzz -M afl-slave -i input -o output -- ./our_qsym/outside_tests/bob @@ /dev/null
    - EVERYTIME Run QSYM in the home directory $ ./qsym/bin/run_qsym_afl.py -a afl-slave -o output -n qsym -- ./our_qsym/outside_tests/pngslap @@
