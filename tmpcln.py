r"""Utility Script for deleteing temporary files form the `Windows` OS `Temp` directory or from current/all user(s) `Local\Temp\` directory.

    - Just envoke the script via a python interpreter or execute the `tmpcln.exe` to clean the temp folders and files.    
"""

from pathlib import Path
from shutil import rmtree
from os import path, unlink, listdir

def get_users(d_users: list[str] = None) -> any:
    """User utility function

        - Return list of users as `str` if no predetermined users list is provided.
        - Return list of user specfic temp-paths if predetermined users list is provided.
    """

    if d_users != None and d_users != []:
        return [f"{usr}\AppData\Local\Temp" for usr in d_users]
    else:
        usrs = [path.join(r"C:\Users", x.name)  for x in Path(r"C:\Users").glob("*") 
                    if x.name not in ["Default", "Default User", "Public", "All Users"] 
                        and x.is_dir()
                ]
        return usrs

def del_file(dir: any = None) -> None:
    """Deletes every file within the provided directory
        - Raises no exception or return value when encounters an error.
    """

    for filename in listdir(dir):
        file_path = path.join(dir, filename)
        try:
            if path.isfile(file_path) or path.islink(file_path):
                unlink(file_path)
            elif path.isdir(file_path):
                rmtree(file_path)
        except:
            continue
    
    return None

def clean_tmp(temp_paths: any = None) -> (Exception | None):
    """wrapper function for deleting files for various paths.
        - Raises a `exception` when encounters an error.
    """

    if temp_paths != None:
        try:
            for path in temp_paths:
                if isinstance(path, list):
                    for dir in path:
                        del_file(dir)
                else:
                    del_file(path)
        except Exception as e:
            return e;
    else:
        return None

def main() -> None:
    print("Deleting Temporary files...")
    deleted = clean_tmp(REMOVEABLE)
    if isinstance(deleted, Exception):
        print(f"Files cannot be deleted! Reason : {deleted}!")
    else:
        print("Files Deleted Successfully! Press 'ENTER' to Exit")
        if input():
            exit(0)

# system wide temp-paths
PREFETCH=r"C:\Windows\Prefetch"
TEMP=r"C:\Windows\Temp"

# sys-users
USERS=get_users(None)

# user specific temp-paths
USER_TEMP=get_users(USERS)

# combined tuple for all temp directories whose content can be removed
REMOVEABLE=(USER_TEMP, TEMP, PREFETCH)

if __name__ == '__main__':
    main()
