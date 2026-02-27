def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def five(n: int) -> bool:
    
    if n <= 0:
        return False
        
  
    while n % 5 == 0:
        n //= 5     
    
    return n == 1

