def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def is_pow_5(n):
    while (n > 1 and n%5 == 0):
	    n//=5
    return n==1
  

def is_prime(num):
    """Перевіряє, чи є число простим."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True