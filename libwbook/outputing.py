
import sys
import os.path
import logging

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
        import subprocess
        base = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        cmd = os.path.join(base, "util", "wbook_say")
        logging.debug("Executing: %r", cmd)
        subprocess.call([cmd, line], close_fds=True)
