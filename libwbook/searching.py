
class Search(object):
    def __init__(self, options):
        pass

    def find(self, line):
        results = []
        #TODO: do real search
        for i in range(15):
            results.append("%s: %s" % (line, i))

        return results

