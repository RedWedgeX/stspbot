# Utilities and helper functions for the bot

def groups(seq, length):
    """Generator to yield groups of the specified length from a sequence. For example, to
    give 10 character chuncks of a string. The final yield will provide whatever data is
    left in the sequence, without any extra padding. Useful in a for statement:
        for pair in groups('abcdefg', 2):
            do_the_thing(pair)
    :param seq: A slicable object like string or list.
    :param length: The length of each group (ie. 2 for pairs)
    """
    for i in range(0, len(seq), length):
        yield seq[i:i + length]


def remove_non_ascii(s):
    """Remove non-ASCII characters from a Unicode string. Removes @ (at symbol, decimal
    64) which pings discord users/roles. Also removes ` (grave accent, decimal 96) which
    modifies discord formatting.
    :param s: String
    """
    return str("".join(i for i in s if ord(i) < 128 and ord(i) != 96 and ord(i) != 64))


def date(target, clock=True):
    if clock is False:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")

