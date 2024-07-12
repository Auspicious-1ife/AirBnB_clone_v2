#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['ubuntu@3.83.253.53', 'ubuntu@100.26.163.202']

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_without_ext = archive_filename.split('.')[0]
        release_folder = f"/data/web_static/releases/{archive_without_ext}"
        
        put(archive_path, f"/tmp/{archive_filename}")

        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_folder}")
        run(f"rm /tmp/{archive_filename}")

        run(f"mv {release_folder}/web_static/* {release_folder}/")
        run(f"rm -rf {release_folder}/web_static")

        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_folder} /data/web_static/current")

        return True
    except Exception as e:
        return False

def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

