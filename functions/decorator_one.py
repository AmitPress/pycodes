def escape_unicode(f):
    def wrapper(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrapper
@escape_unicode
def strfun():
    return "Hello World ∤"
print(strfun())