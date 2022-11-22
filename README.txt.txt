=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program:  \n"
&"No executable file specified.\n"
&"Use the \"file\" or \"exec-file\" command.\n"
^error,msg="No executable file specified.\nUse the \"file\" or \"exec-file\" command."
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f952c2e2ad0>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program:  crashes_qsymgenerated_nov10/README.txt\n"
&"No executable file specified.\n"
&"Use the \"file\" or \"exec-file\" command.\n"
^error,msg="No executable file specified.\nUse the \"file\" or \"exec-file\" command."
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f1a8c0e6810>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap crashes_qsymgenerated_nov10/README.txt\n"
=thread-group-started,id="i1",pid="7208"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 7208) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f528c6e2a50>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"set args crashes_qsymgenerated_nov10/README.txt\n"
=cmd-param-changed,param="args",value="crashes_qsymgenerated_nov10/README.txt"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap crashes_qsymgenerated_nov10/README.txt\n"
=thread-group-started,id="i1",pid="7560"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 7560) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f97342e2ad0>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap \n"
=thread-group-started,id="i1",pid="7907"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 7907) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f57c00e6810>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap \n"
=thread-group-started,id="i1",pid="8055"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 8055) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f34500ea7d0>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap \n"
=thread-group-started,id="i1",pid="8516"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 8516) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7fa0746e27d0>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
=cmd-param-changed,param="logging enabled",value="on"
^done
(gdb) 
&"set args  crashes_qsymgenerated_nov10/README.txt\n"
=cmd-param-changed,param="args",value="crashes_qsymgenerated_nov10/README.txt"
^done
(gdb) 
&"run\n"
~"Starting program: /home/matthewyfong/CSE_5472/CrashDumpPythonScripts/pngslap crashes_qsymgenerated_nov10/README.txt\n"
=thread-group-started,id="i1",pid="8867"
=thread-created,id="1",group-id="i1"
=library-loaded,id="/lib64/ld-linux-x86-64.so.2",target-name="/lib64/ld-linux-x86-64.so.2",host-name="/lib64/ld-linux-x86-64.so.2",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7fd0100",to="0x00007ffff7ff2684"}]
^running
*running,thread-id="all"
(gdb) 
=library-loaded,id="/usr/local/lib/libpng.so.3",target-name="/usr/local/lib/libpng.so.3",host-name="/usr/local/lib/libpng.so.3",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7efeef0",to="0x00007ffff7fb35dc"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libz.so.1",target-name="/lib/x86_64-linux-gnu/libz.so.1",host-name="/lib/x86_64-linux-gnu/libz.so.1",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7edc280",to="0x00007ffff7eecf9b"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libm.so.6",target-name="/lib/x86_64-linux-gnu/libm.so.6",host-name="/lib/x86_64-linux-gnu/libm.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7d983c0",to="0x00007ffff7e3efa8"}]
=library-loaded,id="/lib/x86_64-linux-gnu/libc.so.6",target-name="/lib/x86_64-linux-gnu/libc.so.6",host-name="/lib/x86_64-linux-gnu/libc.so.6",symbols-loaded="0",thread-group="i1",ranges=[{from="0x00007ffff7bbb630",to="0x00007ffff7d3027d"}]
~"[Inferior 1 (process 8867) exited with code 01]\n"
=thread-exited,id="1",group-id="i1"
=thread-group-exited,id="i1",exit-code="01"
*stopped,reason="exited",exit-code="01"
(gdb) 
&"bt\n"
&"No stack.\n"
^error,msg="No stack."
(gdb) 
&"Exception ignored in: <gdb._GdbOutputFile object at 0x7f79f40e27d0>\n"
&"Traceback (most recent call last):\n"
&"  File \"/home/linuxbrew/.linuxbrew/Cellar/gdb/12.1_2/share/gdb/python/gdb/__init__.py\", line 47, in flush\n"
&"    def flush(self):\n"
&"\n"
&"KeyboardInterrupt: \n"
