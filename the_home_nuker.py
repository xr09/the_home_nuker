
import os
import sys
import stat
import shutil
import subprocess


# protected folders in /home
NEVER_DELETE = 'lost+found susan max daisy'.split()

def chmod_writable(func, path, excinfo):
    """ chmod +w file """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def nukedir(path):
    """ Recursive delete (rm -rf) """
    print "Nuking: %s" % path
    shutil.rmtree(path, onerror=chmod_writable)


def get_user_list():
    """
    Returns a list with current logged users and protected folders 
    
    """
    command = subprocess.Popen( ["-c", "who | cut -d' ' -f1 | sort | uniq | grep -v root" ], stdout=subprocess.PIPE, shell=True )
    users, err = command.communicate()
    if users:
        users = [x for x in users.split('\n') if x]
    else:
        users = []
    return set(users).union(set(NEVER_DELETE))


def nuke_all_subdirs():
    """ Delete only subdirectories from a specified path """
    protected_folders = get_user_list()
    path = '/home'
    if not os.path.exists(path):
        sys.exit(0)
    for folder in next(os.walk(path))[1]:
        if folder not in protected_folders:
            # delete folder
            nukedir(os.path.join(path, folder))

if __name__  == "__main__":
    nuke_all_subdirs()
