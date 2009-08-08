
import sys

SEARCH_SEPARATOR = (
        "===============================================================")
SEPARATOR = "---------------------------------------------------------------"

class Outputer(object):
    def __init__(self, options):
        self.back = options.back

    def display(self, bresults, fresults):
        print SEARCH_SEPARATOR
        self._display_results(bresults)
        self._display_results(fresults)

    def _display_results(self, results):
        if results:
            for row in results:
                sys.stdout.write(row)
            print SEPARATOR

    def say(self, line):
        #TODO: start the festival
        print "say:", line
