#!/usr/bin/python3

"""a script that adds all arguments to a Python list,
and then save them to a file."""
import json
import sys


def save_to_json_file(my_obj, filename):
    """adds all arguments to a Python list and saves them to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    filename = "add_item.json"
    items = load_from_json_file(filename)

    # Add the command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
