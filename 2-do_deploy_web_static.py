#!/usr/bin/env python3
"""
Fabric script that distributes an archive to web servers
"""

from fabric.api import env, put, run
import os

# Update the env.hosts variable with your server details
env.hosts = ['ubuntu@3.83.253.53', 'ubuntu@100.26.163.202']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        archive_filename = os.path.basename(archive_path)
        archive_without_ext = archive_filename.split('.')[0]
        release_folder = f"/data/web_static/releases/{archive_without_ext}"

        put(archive_path, f"/tmp/{archive_filename}")

        # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_folder}")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_filename}")

        # Move contents out of the web_static directory
        run(f"mv {release_folder}/web_static/* {release_folder}/")
        run(f"rm -rf {release_folder}/web_static")

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the web server
        run(f"ln -s {release_folder} /data/web_static/current")

        return True
    except Exception as e:
        return False

