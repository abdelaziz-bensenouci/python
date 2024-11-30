L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max = L[0]
min = L[0]

for i in L:
    if i > max:
        max = i
    if i < min:
        min = i

print("Valeur max : ", max)
print("Valeur min : ", min)


#2eme solution
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max_value = max(L)
print(max_value)