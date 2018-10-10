import sys

args = sys.argv
n = int(args[1])

dx = 1.0 / n
def func(x):
  return 1 / (x**2 + 1)

sum = 0.0
for i in range(0, n):
  x1 = i * dx
  x2 = x1 + dx
  sum += (func(x1) + func(x2)) * dx / 2.0

pi = sum * 4.0
print pi

