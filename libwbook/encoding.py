
import locale

ENCODING = locale.getpreferredencoding() or 'ascii'

def incode(inbytes):
    return unicode(inbytes, ENCODING)

def out(text):
    return text.encode(ENCODING)

