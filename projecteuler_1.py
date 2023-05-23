sum = 0

for k in range(1,1000,1):
    if (k%3==0) or (k%5==0):
        sum = sum + k
        print(sum)


