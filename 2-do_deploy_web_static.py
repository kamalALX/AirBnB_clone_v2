#!/usr/bin/python3
""" a Fabric script that
- distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.25.165.190', '54.162.91.137']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False


    try:
        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')

        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, archive_name))

        run("rm /tmp/{}".format(archive_filename))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, archive_name))
        run('rm -rf {}{}/web_static'.format(path, archive_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, archive_name))
        return True
    except:
        return False
