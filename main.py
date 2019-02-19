import json
import pprint
import tkinter as tk
from tkinter import filedialog


def object_from_url(url):
    '''
    (str) -> object

    Precondition: object must be dict or list type

    Return an object represented by json located at url
    '''
    with urllib.request.urlopen(url) as f:
        return json.load(f)


def object_from_file(filename):
    '''
    (str) -> object

    Precondition: object must be dict or list type

    Return an object represented by json located in file
    '''
    with open(filename) as f:
        return json.load(f)


def get_part(object, part):
    '''
    (object) -> object

    Precondition: part must be hashable type, object must be list, tuple, str,
    or dict

    Return a record in object by 'part' key
    '''
    return object[part]


def main():
    '''
    () -> None

    Main function of the program.
    '''
    print('Select a json file to view\n')
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        pprint.pprint(object_from_file(file_path))
    else:
        print('No file selected')
    input('\nPress Enter to quit. ')

main()
