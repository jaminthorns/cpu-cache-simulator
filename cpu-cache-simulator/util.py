import random


def rand_byte():
    """Get a random byte.

    :return: random byte (integer from 0 - 255)
    """
    return random.randint(0, 0xFF)


def dec_str(integer, width):
    """Get decimal formatted string representation of an integer.

    :param int byte: integer to be converted to decimal string
    :return: decimal string representation of integer
    """
    return "{0:0>{1}}".format(integer, width)


def bin_str(integer, width):
    """Get binary formatted string representation of an integer.

    :param int byte: integer to be converted to binary string
    :return: binary string representation of integer
    """
    return "{0:0>{1}b}".format(integer, width)


def hex_str(integer, width):
    """Get hexadecimal formatted string representation of an integer.

    :param int byte: integer to be converted to hexadecimal string
    :return: hexadecimal string representation of integer
    """
    return "{0:0>{1}X}".format(integer, width)
