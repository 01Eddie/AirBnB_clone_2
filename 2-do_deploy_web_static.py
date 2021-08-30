#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers"""
import fabric
from fabric.api import local, env, put, run
from datetime import datetime
from os import path

env.hosts = ['35.237.172.160', '35.237.222.103']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ * Prototype: def do_deploy(archive_path):
    * Returns False if the file at the path archive_path doesn’t exist
    * The script should take the following steps:
    ** Upload the archive to the /tmp/ directory of the web server
    ** Uncompress the archive to the folder
    /data/web_static/releases/<archive filename without extension> on the web
    server
    ** Delete the archive from the web server
    ** Delete the symbolic link /data/web_static/current from the web server
    ** Create a new the symbolic link /data/web_static/current on the web
    server, linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
    * All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    * Returns True if all operations have been done correctly,
    otherwise returns False
    * You must use this script to deploy it on your
    servers: xx-web-01 and xx-web-02
    In the following example, the SSH key and the username used for accessing
    to the server are passed in the command line. Of course, you could define
    them as Fabric environment variables (ex: env.user =...)

    Disclaimer: commands execute by Fabric displayed below are linked to the
    way we implemented the archive
    function do_pack
    - like the mv command
    - depending of your implementation of it, you may don’t need it """

    if not path.exists(archive_path):
        return False
    try:
        NameArchive = archive_path.split('/')[-1]
        NameArchiveWitoutExtension = NameArchive.replace('.tgz', '')
        put(archive_path, "/temp/")
        run("sudo mkdir -p /data/web_static/releases/" + NameArchiveWitoutExtension)
        run("sudo tar -xzvf /tmp/" + NameArchive + " -C /data/web_static/releases/")
        run("sudo rm -rf /tmp/" + NameArchive)

        run("sudo mv /data/web_static/releases/web_static/* /data/web_static/releases/")
        run("sudo rm -rf /data/web_static/releases/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/ /data/web_static/current")

        return True
    except Exception:
        return False
