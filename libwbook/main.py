"""\
Usage: %prog [options] [word]
Finds the given word in the dictionary.\
"""

import logging
import optparse

from libwbook import inputing, searching, outputing, encoding
from libwbook.dating import apppath

DEFAULT_DICT = apppath("data", "english.dict")
DEFAULT_BACK = 3
DEFAULT_FORTH = 15
DEFAULT_QUIET = False

def _parse_args():
    parser = optparse.OptionParser(__doc__)
    parser.add_option("-d", "--dict",
            help="use DICT (default=%s)" % DEFAULT_DICT)
    parser.add_option("-b", "--back", type="int",
            help="print BACK words back (default=%s)" % DEFAULT_BACK)
    parser.add_option("-f", "--forth", type="int",
            help="print FORTH words forth (default=%s)" % DEFAULT_FORTH)
    parser.add_option("-q", "--quiet", action="store_true",
            help="don't run say (default=%s)" % DEFAULT_QUIET)
    parser.add_option("-v", "--verbose", action="store_true",
            help="enable debug output")
    parser.add_option("-e", "--encoding",
            help="use this input/output encoding (default=%s)" %
            encoding.ENCODING)
    parser.set_defaults(back=DEFAULT_BACK, forth=DEFAULT_FORTH,
            dict=DEFAULT_DICT, quiet=DEFAULT_QUIET)

    options, args = parser.parse_args()
    if options.encoding:
        encoding.ENCODING = options.encoding

    if options.verbose:
        level = logging.DEBUG
    else:
        level = logging.WARNING
    logging.basicConfig(level=level)

    return options, args

def main():
    options, args = _parse_args()
    arg_bytes = " ".join(args)

    search = searching.Search(options)
    reader = inputing.Reader(search, arg_bytes)
    outputer = outputing.Outputer(options)
    try:
        while True:
            line = reader.read_line()
            bresults, fresults = search.find(line)
            outputer.display(bresults, fresults)
            outputer.say(line)

    except EOFError:
        print "OK, bye."
