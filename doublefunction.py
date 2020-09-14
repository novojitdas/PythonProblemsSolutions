def outer(a, b):
    def inner(a, b):
        return a+b

    add = inner(a, b)
    return add+5


print("start")
print(outer(5, 10))
