
import os.path
import unicodedata

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
        return (
                _asresults(self.dictionary[start:index]),
                _asresults(self.dictionary[index:end]))

    def find_forth(self, line, max_results):
        """Returns forth_results for the given line.
        """
        index = _search_up(self.dictionary, line)
        end = index + max_results
        return _asresults(self.dictionary[index:end])

def _asresults(rows):
    """Decodes (orig, translated) from each row.
    """
    results = []
    for row in rows:
        orig, translated, rest = row.split("\0")
        assert rest == "\n"
        orig = orig.rstrip()
        translated = translated.rstrip()
        results.append((orig, translated))

    return results

def _search_up(items, x):
    """Finds the index of x or before any value bigger than x.
    """
    # Taken from the bisect_left()
    lo = 0
    hi = len(items)
    while lo < hi:
        mid = (lo+hi)//2
        if _compare(items[mid], x) < 0: lo = mid+1
        else: hi = mid
    return lo

def startswith(result, line):
    return _normalize(result).startswith(_normalize(line))

def _compare(row, line):
    return cmp(_normalize(row), _normalize(line))

def _normalize(text):
    """Normalizes the text for sorting.
    """
    return _separate_accents(text.lower())

def _separate_accents(text):
    """Moves an accent after its letter.
    So sorting will place an accented letter after non-accented one.
    The dictionaries are sorted the same way.
    """
    chars = []
    for c in unicodedata.normalize("NFD", text):
        chars.append(c)
    return "".join(chars)

class _FileAsList(object):
    def __init__(self, filename, line_width=82, file_encoding="iso-8859-2"):
        self.file = open(filename)
        self.line_width = line_width
        self.len = os.path.getsize(filename)//line_width
        self.file_encoding=file_encoding

    def __getitem__(self, index):
        if isinstance(index, slice):
            indices = index.indices(self.len)
            return [self[i] for i in xrange(*indices)]
        else:
            self.file.seek(self.line_width * index)
            return unicode(self.file.read(self.line_width), self.file_encoding)

    def __len__(self):
        return self.len

