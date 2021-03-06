import sys
import math

args = sys.argv
n = int(args[1])

dx = 1.0 / n
def func(x):
  return 1 / (x**2 + 1)

sum = 0.0
for i in range(0, n):
  x = i * dx
  sum += func(x) * dx

pi = sum * 4.0
err = math.pi - pi

print "pi          :", math.pi
print "approximate :", pi
print "error       :", err

