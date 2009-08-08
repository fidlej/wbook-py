
import bisect
import os.path

class Search(object):
    def __init__(self, options):
        self.back = options.back
        self.forth = options.forth
        self.dictionary = _FileAsList(options.dict)

    def find(self, line):
        index = bisect.bisect_left(self.dictionary, line)
        start = max(0, index - self.back)
        end = index + self.forth
        results = [self.dictionary[i] for i in xrange(start, end)]
        return self.dictionary[start:end]

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

