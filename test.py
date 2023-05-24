#!/usr/bin/env python
 
import os, sys
 
mypipe = '/tmp/tmp_file.txt'
 
def parent():
    f = open(mypipe, "r")
    acc = ''
    while True:
        try:
            s = f.read()
        except IOError as e:
            sys.stderr.write("IO ERROR: %s\n" % e.strerror)
            break
        acc += s
        if len(s) == 0:
            break
    f.close()
    sys.stderr.write("Result:\n")
    print(acc)
 
 
def child():
    os.chdir(os.environ['HOME'])
    prog = './ch12'
    os.execv(prog, [prog])
 
if not os.path.exists(mypipe):
    os.umask(0111)
    os.mkfifo(mypipe, 0666)
 
pid = os.fork()
 
if pid > 0:
    parent()
    os.waitpid(pid)
else:
    child()
