
import readline

class Reader(object):
    def __init__(self, line=""):
        self.line = line

    def read_line(self):
        if self.line:
            line = self.line
            self.line = ""
            return line

        return raw_input("wbook> ")

