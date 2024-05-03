#!/usr/bin/python3
""" a Fabric script that
- distributes an archive to your web servers, using the function do_deploy
"""
from datetime import datetime
from os.path import exists


def do_deploy():
    if not exists(archive_path):
        return False

    else:
        put()
