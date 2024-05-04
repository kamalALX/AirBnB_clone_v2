#!/usr/bin/python3
""" a Fabric script that
- distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.25.165.190']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_apath, '/home')
    except:
        return False
