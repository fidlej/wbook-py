
import readline

class Reader(object):
    def __init__(self, line="", input_encoding="utf-8"):
        self.line = line
        self.input_encoding = input_encoding

    def read_line(self):
        if self.line:
            line = self.line
            self.line = ""
            return line

        return unicode(raw_input("wbook> "), self.input_encoding)

