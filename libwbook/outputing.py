
import sys

class Outputer(object):
    def __init__(self, options):
        pass

    def display(self, results):
        for row in results:
            sys.stdout.write(row)

    def say(self, line):
        #TODO: start the festival
        print "say:", line
