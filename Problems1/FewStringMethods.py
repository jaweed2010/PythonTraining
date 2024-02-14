def uppr(s):
    return s.upper()


def pad_front(s):
    return s.zfill(10)

'''
splits a string into a list.

You can specify the separator, default separator is any whitespace.
'''
def tokenize(s):
    return s.split(',')



'''
takes all items in an iterable and joins them into one string.

A string must be specified as the separator
'''
def list_to_string(x):
    return ''.join(str(x))


print(uppr("hello"))
print(pad_front("hello"))
print(tokenize("abc,def,ghi"))
print(list_to_string([1,2,3]))