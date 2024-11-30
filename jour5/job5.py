L = [1, 2, 3, 4, 5]
print(L)
print(L[1])

def modificationTab():
    L[3] = L[2] + L[4]
    return L
modificationTab()
print(L)
print(L[4])

