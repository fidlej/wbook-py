
import sys
import os.path
import logging

SEARCH_SEPARATOR = (
        "===============================================================")
SEPARATOR = "---------------------------------------------------------------"

class Outputer(object):
    def __init__(self, options, output_encoding="utf-8"):
        self.back = options.back
        self.output_encoding = output_encoding

    def display(self, bresults, fresults):
        print SEARCH_SEPARATOR
        self._display_results(bresults)
        self._display_results(fresults)

    def _display_results(self, results):
        if results:
            for row in results:
                sys.stdout.write(row.encode(self.output_encoding))
            print SEPARATOR

    def say(self, line):
        import subprocess
        base = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        cmd = os.path.join(base, "util", "wbook_say")
        args = [cmd, line]
        logging.debug("Executing: %r", args)
        subprocess.call(args, close_fds=True)
