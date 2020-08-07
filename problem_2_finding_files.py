"""
the goal is to write code for finding all files under a 
directory (and all directories beneath it) that end with ".c"
"""

import os

def find_files_subdir(suffix, path, files):
    for f in os.listdir(path):
        subpath = os.path.join(path, f)
        if os.path.isdir(subpath):
            files = find_files_subdir(suffix, subpath, files)
        elif os.path.isfile(subpath) and (f.endswith(suffix) or f is None):
            files.append(subpath)

    return files

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    path_list = list()

    if not bool(path) or not bool(suffix):
        print("ERROR: no path or suffix specified")
        return path_list

    path_list = find_files_subdir(suffix, path, path_list)

    return path_list


if __name__=="__main__":
    # no data test
    # find_files("", "")
    # find_files(".c", "")
    # find_files(".c", None)
    # find_files(None, "./testdir")

    # dir-test case
    print(find_files(".c", "./testdir"))