#!/usr/bin/python3
#a Fabric script that generates a .tgz archive from the
#contents of the web_static folder of your AirBnB Clone repo.

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Archives the static files."""
    cur_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
