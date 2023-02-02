#!/usr/bin/env python
# (c) 2016 John Strickler
#
"""
Routines to convert Unix-style line endings to DOS.
"""
import re
import logging

logger = logging.getLogger(__name__)

RE_EOL = re.compile(r'(?<!\x0D)\x0A')

def convert_to_dos(file_name):
    """
    Convert line endings from Unix style (\\\\x0A) to DOS style (\\\\x0D0A).
    Files are converted in place.


    :param file_name: File name to convert.
    :return: None
    """
    logger.debug("Converting %s to DOS", file_name)
    if file_name.endswith(('.jpg', '.png', '.bmp', '.jpeg')):
        return

    with open(file_name, 'r') as file_in:
        try:
            contents = file_in.read()
        except UnicodeDecodeError:
            logger.warning(f"{file_name} is not a text file")
            return

    with open(file_name, 'w') as file_out:
        file_out.write(RE_EOL.sub('\x0D\x0A', contents))
