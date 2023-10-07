#!/usr/bin/python3
"""
this script fot Delete out-of-date
fab -f: do_clean:number=2
    -i: ssh-key -u: ubuntu  /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['54.237.114.58', '100.25.190.26']


def do_clean(number=0):
    """this for Delete out-of-date.
    Args:
        number (int): for The num of archives to keep.
    If num is 0 or 1, keeps only the most recent. If
    num is 2, keeps and second-most recent,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
