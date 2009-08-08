
class Outputer(object):
    def __init__(self, options):
        pass

    def display(self, results):
        for line in results:
            print line

    def say(self, line):
        #TODO: start the festival
        print "say:", line
