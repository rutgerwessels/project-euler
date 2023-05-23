x=0
number = 10

while x < 1:
    if all(number%k==0 for k in range(1,21,1)):
       print(number)
       x=1
    else:
       number = number+1
           
