#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers"""
import fabric
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['35.237.172.160', '35.237.222.103']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ * Prototype: def do_deploy(archive_path):
    - depending of your implementation of it, you may don’t need it """

    """if not path.exists(archive_path):
        return False"""
    try:
        NameArchive = archive_path.split('/')[-1]
        NameArchiveWitoutExtension = NameArchive.replace('.tgz', '')
        put(archive_path, "/tmp/")
        dr = "/data/web_static/releases/"
        run("sudo mkdir -p " + dr + NameArchiveWitoutExtension)
        run("sudo tar -xzvf /tmp/" + NameArchive + " -C " + dr)
        run("sudo rm -rf /tmp/" + NameArchive)
        r = "/data/web_static/"
        run("sudo mv " + r + "releases/web_static/* " + r + "releases/")
        run("sudo rm -rf " + r + "releases/web_static")
        run("sudo rm -rf " + r + "current")
        run("sudo ln -sf " + r + "releases/ " + r + "current/")

        return True
    except Exception:
        return False
