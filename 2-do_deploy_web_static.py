#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api import env, put, run, sudo
from os.path import exists
env.hosts = ['100.25.117.41', '100.25.220.30']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive filename without extension>
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        sudo('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, folder_name))

        # Delete archive from /tmp/
        sudo('rm /tmp/{}'.format(archive_name))

        # Delete symbolic link /data/web_static/current
        sudo('rm -f /data/web_static/current')

        # Create new symbolic link /data/web_static/current
        sudo('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        return True
    except:
        return False
