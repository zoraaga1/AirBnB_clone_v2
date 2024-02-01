#!/usr/bin/python3
"""do_deploy module"""

import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers,
    using the function do_deploy:
    """
    if os.path.isfile(archive_path) is False:
        return False
    f = archive_path.split("/")[-1]
    n = f.split(".")[0]

    if put(archive_path, "/tmp/{}".format(f)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(n)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(n)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(f, n)).failed is True:
        return False
    if run("rm /tmp/{}".format(f)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(n, n)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(n)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(n)).failed is True:
        return False
    return True
