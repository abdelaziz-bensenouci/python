def est_premier(n):
    """Détermine si un nombre est premier."""
    if n <= 1:  
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False
    return True  

for num in range(2, 1001):  
    if est_premier(num):
        print(num)