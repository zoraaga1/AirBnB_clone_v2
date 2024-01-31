#!/usr/bin/python3
"""do_pack module"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz archive from the contents
    of the web_static folder"""
    t_now = datetime.utcnow()
    f = "versions/web_static_{}{}{}{}{}{}.tgz".format(t_now.year,
                                                         t_now.month,
                                                         t_now.day,
                                                         t_now.hour,
                                                         t_now.minute,
                                                         t_now.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(f)).failed is True:
        return None
    return f
