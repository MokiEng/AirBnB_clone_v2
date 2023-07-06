#!/usr/bin/python3
"""
a Fabric script that distributes an archive to your web servers,
using the function do_deploy:
"""
from os.path import exists
from datetime import datetime
from fabric.api import env, local, put, run, 

env.hosts = ["34.234.204.250", "54.197.49.59"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
     if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        filename = archive_path.split('/')[-1]
        folder_name = filename.split('.')[0]

        # Create the release folder
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))

        # Uncompress the archive to the release folder
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move the contents of the release folder to the parent folder
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))

        # Remove the now empty web_static folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
