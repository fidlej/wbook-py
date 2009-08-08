
import sys

SEARCH_SEPARATOR = (
        "===============================================================")
SEPARATOR = "---------------------------------------------------------------"

class Outputer(object):
    def __init__(self, options):
        self.back = options.back

    def display(self, results):
        print SEARCH_SEPARATOR
        for i, row in enumerate(results):
            if i == self.back:
                print SEPARATOR
            sys.stdout.write(row)

        print SEPARATOR

    def say(self, line):
        #TODO: start the festival
        print "say:", line
