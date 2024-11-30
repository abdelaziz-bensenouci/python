L = [1, 2, 3, 4, 5]
print(L)

def echangeTab():
    L[0], L[4] = L[4], L[0]
    return L
echangeTab()
print(L)