import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())


d = int(input())
a, b, c = get_ints()

e = a + b + c
f = d-e
print(f)
