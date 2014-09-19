# This is a relatively simple script that will examine some environmental
# variables, log in to iRODS, mount the file system, and then execute the
# script passed in.

import os
import sys
import subprocess

# Now let's set up our environment
os.environ.setdefault("irodsUserName", "rods")
os.environ.setdefault("irodsPass", "rods")
os.environ.setdefault("irodsHost", "localhost")
os.environ.setdefault("irodsPort", "8547")
os.environ.setdefault("irodsZone", "tempZone")

p = subprocess.Popen(["iinit"], stdin=subprocess.PIPE)
p.stdin.write(os.environ.pop("irodsPass"))
p.communicate()
assert(not p.returncode)

if not os.path.exists("fuse"):
    os.mkdir("fuse")
p = subprocess.Popen(["irodsFs", "fuse"])
p.communicate()
assert(not p.returncode)

os.chdir("fuse")
os.execlp("python2.7", "", sys.argv[1])
