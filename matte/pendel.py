import math
t = 0
v = 0
l = 1
a = 89
s = l*a

while t < 5:
    v = v - 9.82 * math.sin(s/l) * 0.001
    s = s + v*0.001
    t = t + 0.001
    print(v)
