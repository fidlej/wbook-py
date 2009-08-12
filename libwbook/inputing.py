
import sys
import readline
import logging

from libwbook.encoding import incode, out
from libwbook import searching

class Reader(object):
    def __init__(self, search, arg_bytes=""):
        self.line = incode(arg_bytes)
        _set_completer(search)

    def read_line(self):
        if self.line:
            line = self.line
            self.line = ""
            readline.add_history(line)
            return line

        return incode(raw_input("wbook> "))

def _set_completer(search):
    readline.set_completer_delims("")
    readline.set_completer(LineCompleter(search).complete)
    readline.parse_and_bind("tab: complete")

class LineCompleter(object):
    MAX_RESULTS = 100
    def __init__(self, search):
        self.search = search
        self.results = []

    def complete(self, inbytes, state):
        try:
            return self._complete(inbytes, state)
        except Exception:
            logging.exception("complete problem: %s, %s", inbytes, state)
            return None

    def _complete(self, inbytes, state):
        text = incode(inbytes)
        if state == 0:
            self.results = self.search.find_forth(text, self.MAX_RESULTS)

        if state >= len(self.results):
            return self._stop(state)

        orig, translated = self.results[state]
        result = _rstrip_extra(orig, len(text))
        if searching.startswith(result, text):
            return out(result)

        logging.debug("complete stop: %s, %s, %r", inbytes, state, result)
        return self._stop(state)

    def _stop(self, state):
        self.results = []
        return None

def _rstrip_extra(result, input_len):
    """It strips the trailing spaces from the result,
    if they are after the input length.
    """
    return result[:input_len] + result[input_len:].rstrip()
