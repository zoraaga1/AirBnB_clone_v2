#!/usr/bin/python3
"""Fabric script to clean up outdated archives"""
from fabric.api import *


env.hosts = ['18.207.1.146', '54.89.16.211']
env.user = "ubuntu"


def do_clean(number=0):
    """Delete out-of-date archives"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))