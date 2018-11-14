import sys
import math

args = sys.argv
n = int(args[1])

dx = 1.0 / n

def f(x):
  return 1.0 / (x**2 + 1.0)

sum = 0.0
for i in range(0, n+1):
  if i == 0 or i == n:
    w = 1.0
  elif i % 2 == 1:
    w = 4.0
  else:
    w = 2.0
  x = i * dx
  sum += dx * w * f(x) / 3.0

pi = sum * 4.0

print pi

