#!/usr/bin/env python3
"""
 fabric script based on the task 0 file that creates and
 distributes as archive to the webservers
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    All archives must be stored in the folder versions.
    The name of the archive created must be web_static_
    <year><month><day><hour><minute><second>.tgz.
    Returns the archive path if the archive has been correctly generated,
    otherwise returns None.
    """
    # Creates versions directory if it doesn't exist
    local('sudo mkdir -p versions')

    t = datetime.now()
    t_str = t.strftime('%Y%m%d%H%M%S')

    local(f'sudo tar -cvzf versions/web_static_(t_str).tgz web_static')


    
