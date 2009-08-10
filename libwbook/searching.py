
import os.path

class Search(object):
    def __init__(self, options):
        self.back = options.back
        self.forth = options.forth
        self.dictionary = _FileAsList(options.dict)

    def find(self, line):
        """Returns (back_results, forth_results)
        for the given line.
        """
        index = _search_up(self.dictionary, line)
        start = max(0, index - self.back)
        end = index + self.forth
        results = [self.dictionary[i] for i in xrange(start, end)]
        return self.dictionary[start:index], self.dictionary[index:end]

def _search_up(items, x):
    """Finds the index that is before any value equal to x.
    """
    # Taken from the bisect_left()
    lo = 0
    hi = len(items)
    while lo < hi:
        mid = (lo+hi)//2
        if _compare(items[mid], x) < 0: lo = mid+1
        else: hi = mid
    return lo

def _compare(line, word):
    return cmp(line.lower(), word.lower())

class _FileAsList(object):
    def __init__(self, filename, line_width=82):
        self.file = open(filename)
        self.line_width = line_width
        self.len = os.path.getsize(filename)//line_width

    def __getitem__(self, index):
        if isinstance(index, slice):
            indices = index.indices(self.len)
            return [self[i] for i in xrange(*indices)]
        else:
            self.file.seek(self.line_width * index)
            return self.file.read(self.line_width)

    def __len__(self):
        return self.len

