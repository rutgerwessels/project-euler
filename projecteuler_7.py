primes=[2]
k=3

while len(primes) < 10001:
    if all(k%p != 0 for p in primes):
        primes.append(k)        
    k=k+1
    
print(primes[-1])    
