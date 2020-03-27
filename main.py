import os
import argparse

from impacket.examples import *


if os.path.isfile("config"):
    configfile = True
else:
    f = open("config", "a+")
    f.write("ip = ''\n")
    f.write("port = ''\n")
    f.write("username = ''\n")
    f.write("password=''\n")
    f.write("path = ''\n")
    f.write("domain = ''\n")
    f.write("no-pass = 'False'\n")
    f.write("hash = ''\n")
    f.write("aesKey = ''\n")
    f.write("debug = 'False'\n")
    f.write("sam = ''\n")
    f.write("userfile = '<user file name>'\n")
    f.write("passwordfile ='<password file name>'\n")

    f.close()

"""

ARGS here

"""


config = open("config", "a")


#import subprocess
#subprocess.Popen("psexec.py test@127.0.0.1", shell=True)

