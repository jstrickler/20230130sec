"""
Read knight data

Description of what's happening in this script....
"""
from pprint import pprint

def main():
    """
    Program entry point

    :return: None
    """
    data = get_data()
    pretty_print(data)
    print()
    print_titles(data)

def get_data():
    """
    Read data from text file and parse it out into fields.


    :return: Dictionary of knight data
    """
    knight_data = {}
    with  open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            if quest == '':
                quest = None
            knight_data[name] = (title, color, quest, comment)
    return knight_data

def pretty_print(knight_data):
    """
    Print data in readable form.

    :param knight_data: Dictionary of knight data
    :return: None
    """
    pprint(knight_data)

def print_titles(knight_data):
    """
    Print just titles and names of knights.

    :param knight_data: Dictionary of knight data
    :return: None
    """
    for knight, data in knight_data.items():
        print(data[0], knight)

main()
