#!/usr/bin/python3
"""
A module for web application deployment
Usage: fab -f 100-clean_web_static.py do_clean:number=2 -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

# Define the hosts
env.hosts = ['100.25.117.41', '100.25.220.30']


def do_clean(number=0):
    """
    Archives the static files.
    
    Args:
        number (int): The number of archives to keep.
        
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives, etc.
    """
    number = max(1, int(number))  # Ensure number is at least 1

    # Delete local archives
    local_archives = sorted(os.listdir("versions"))
    local_archives_to_delete = local_archives[:-number]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in local_archives_to_delete]

    # Delete remote archives
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        remote_archives_to_delete = remote_archives[:-number]
        [run("rm -rf ./{}".format(a)) for a in remote_archives_to_delete]
