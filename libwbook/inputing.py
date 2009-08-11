
import readline

class Reader(object):
    def __init__(self, line="", input_encoding="utf-8"):
        self.line = unicode(line, input_encoding)
        self.input_encoding = input_encoding

    def read_line(self):
        if self.line:
            line = self.line
            self.line = ""
            readline.add_history(line)
            return line

        return unicode(raw_input("wbook> "), self.input_encoding)
