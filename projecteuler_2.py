u = 1
v = 2
w = 0
sum_even = 2

while v < 4000000:
    w = u + v
    if w%2 == 0:
        sum_even = sum_even + w
    u = v
    v = w

print(sum_even)
