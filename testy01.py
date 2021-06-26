a = ('foo', 'bar', 'baz', 'qux')
b = ('baz', 'qux', 'bar', 'foo')
if a == b:
    print("equal")
else:
    print("not equal")
    print('qux' in a)
    print('qix' in a)
    print('qix' not in a)
