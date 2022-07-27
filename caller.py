# Pass args in python to the One file to another file.
import os, time
from subprocess import Popen
import subprocess

cmd= ['python', 'RunWithArgs.py']
p = Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
p.stdin.write('Python \n')
p.stdin.write("~15 Yrs \n")
output = p.communicate()[0]
print("My Details \n",output)


