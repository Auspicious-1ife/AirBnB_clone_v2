#!/usr/bin/python3
"""
 fabric script based on the task 0 file that creates and distributes as archive to the webservers
"""
from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    All archives must be stored in the folder versions.
    The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz.
    Returns the archive path if the archive has been correctly generated, otherwise returns None.
    """
    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        print("web_static packed: {} -> {}Bytes".format(archive_name, os.path.getsize(archive_name)))
        return archive_name
    except Exception as e:
        print("An error occurred while creating the archive: {}".format(e))
        return None

