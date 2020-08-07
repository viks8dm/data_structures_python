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
        # print("ERROR: no path or suffix specified")
        return path_list

    # check if path has suffix, if yes add it to pth_list
    if (not os.path.isdir(path)):
        filename, file_extension = os.path.splitext(path)
        if file_extension != '':
            path_list.append(path)
            return path_list

    
    path_list = find_files_subdir(suffix, path, path_list)

    return path_list


if __name__=="__main__":
    # test-1
    print("------------- test set - 1: no or incorrect data cases")
    print("Pass" if find_files("", "")==[] else "FAIL")
    print("Pass" if find_files(".c", "")==[] else "FAIL")
    print("Pass" if find_files(".c", None)==[] else "FAIL")
    print("Pass" if find_files(".c", False)==[] else "FAIL")
    print("Pass" if find_files(None, "./testdir")==[] else "FAIL")
    print("Pass" if find_files(".md", '')==[] else "FAIL")
    print("Pass" if find_files(".h", '')==[] else "FAIL")

    output_1 = ['./testdir/subdir5/a.h']    
    print("Pass" if find_files(".h", './testdir/subdir5/a.h')==output_1 else "FAIL")

    print("------------- test set - 2: known data cases")
    output_2 = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
    print("Pass" if find_files(".c", "./testdir")==output_2 else "FAIL")


