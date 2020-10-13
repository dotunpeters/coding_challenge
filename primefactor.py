"""
############### Pseudocode ##############
value = N
factors = list()
while N > 1:
    i = 0
    if sympy.isprime(i) and N % prime[i] == 0:
        factors.append(prime[i])
        N = int(N/prime[i])
    else:
        i += 1
return factors
"""
import sympy

def primeFact(N):
    factors = list()
    i = 2
    while N > 1:
        if sympy.isprime(i) and N % i == 0:
            factors.append(i)
            N = int(N/i)
        else:
            i += 1
    return factors

print(primeFact(int(input("Number: "))))