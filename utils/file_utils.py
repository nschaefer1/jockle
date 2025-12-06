import csv
import os



def read_basic_file(path):
    '''
    Reads a text-based file (.txt, .sql, or similar) and returns its contents.

    Parameters
    ----------
    path : str
        Path to the file to read.

    Returns
    -------
    str
        The full contents of the file as a single string.
    '''
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_txt(data, path: str):
    '''
    Writes text to a file, replacing any existing contents.

    Parameters
    ----------
    data : str
        The text to write into the file.

    path : str
        Destination file path.

    Returns
    -------
    None
        The function does not return a value.
    '''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

def load_csv(path):
    '''
    Loads a CSV file and returns its rows as a list of dictionaries.

    Libraries
    ----------
    import csv

    Parameters
    ----------
    path : str
        File system path to the CSV file.

    Returns
    -------
    list[dict]
        A list where each element represents a row from the CSV,
        with column headers mapped to their corresponding values.
    '''
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def file_walker(root, ext=None, mode=None):
    '''
    Walks all files under a given root directory and returns paths. 

    Libraries
    ----
    import os

    Parameters
    ----
    root : str
        The starting directory to walk.

    ext : str, optional
        If provided, only files ending with the extension are returned (e.g., 'png').

    mode: str, optional
        Controls how returned paths are formatted:
        - None (default): full normalized file paths.
        - 'relative': paths relative to the given root.
        - 'uri': file paths formatted as file:/// URIs.

    Returns
    ----
    list[str]
        A list of file paths formatted according to the selected mode.
    '''

    paths = []
    root_norm = os.path.abspath(root).replace('\\','/')

    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            # Skip files not matching the given extension
            if ext is not None and not name.lower().endswith(ext.lower()):
                continue
            # Remove backward slashes cuz we don't like those
            full_path = os.path.join(dirpath, name)
            normalized = os.path.abspath(full_path).replace('\\','/')
            # --- mode handling ---
            if mode == 'relative':
                trimmed = normalized.replace(root_norm + '/', '')
                paths.append(trimmed)
            elif mode == 'uri':
                drive, rest = os.path.splitdrive(normalized)
                drive = drive.upper() 
                uri = f"file:///{drive}{rest}"
                paths.append(uri)
            else:
                paths.append(normalized)

    return paths
