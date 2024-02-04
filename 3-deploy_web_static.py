#!/usr/bin/python3
"""Fabric script to generate and distribute an archive to web servers"""
from fabric.api import *
from os import path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['18.207.1.146', '54.89.16.211']

def do_pack():
    """Create a compressed archive of web_static files"""
    try:
        now = datetime.now()
        formatted_time = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(formatted_time)
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """Distribute archive to web servers"""
    if not path.exists(archive_path):
        return False

    try:
        archive_name = path.basename(archive_path)
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name[:-4]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, archive_name[:-4]))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_name[:-4],
                                                   archive_name[:-4]))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_name[:-4]))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name[:-4]))
        print("New version deployed!")
        return True
    except Exception as e:
        return False

def deploy():
    """Deploy archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
