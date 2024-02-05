#!/usr/bin/python3
"""Fabric script to create and distribute an archive to web servers"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['18.207.1.146', '54.89.16.211']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder"""
    t_now = datetime.utcnow()
    f = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        t_now.year,
        t_now.month,
        t_now.day,
        t_now.hour,
        t_now.minute,
        t_now.second
    )
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(f)).failed is True:
        return None
    return f


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if archive_path is None or os.path.isfile(archive_path) is False:
        return False

    file_name = os.path.basename(archive_path)
    remote_path = "/tmp/{}".format(file_name.split(".")[0])

    put(archive_path, '/tmp/')
    run("mkdir -p {}".format(remote_path))
    run("tar -xzf /tmp/{} -C {}".format(file_name, remote_path))
    run("rm /tmp/{}".format(file_name))
    run("mv {}/web_static/* {}".format(remote_path, remote_path))
    run("rm -rf {}/web_static".format(remote_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(remote_path))

    return True


def deploy():
    """Deploy the web_static content to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
