
import sys
import logging

from libwbook.encoding import out
from libwbook.dating import apppath

SEARCH_SEPARATOR = (
        "===============================================================")
SEPARATOR = "---------------------------------------------------------------"

class Outputer(object):
    def __init__(self, options):
        self.back = options.back
        self.quiet = options.quiet

    def display(self, bresults, fresults):
        print SEARCH_SEPARATOR
        self._display_results(bresults)
        self._display_results(fresults)

    def _display_results(self, results):
        if results:
            for row in results:
                sys.stdout.write(out(row))
            print SEPARATOR

    def say(self, line):
        if self.quiet:
            return

        import subprocess
        cmd = apppath("util", "wbook_say")
        args = [cmd, line]
        logging.debug("Executing: %r", args)
        subprocess.call(args, close_fds=True)
