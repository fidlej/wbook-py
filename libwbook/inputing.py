
import readline

from libwbook.encoding import incode

class Reader(object):
    def __init__(self, arg_bytes=""):
        self.line = incode(arg_bytes)

    def read_line(self):
        if self.line:
            line = self.line
            self.line = ""
            readline.add_history(line)
            return line

        return incode(raw_input("wbook> "))
