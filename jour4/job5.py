def calcule(num1, operator, num2):
    if operator == "*":
        return(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            return(num1 / num2)
        else:
            return("Erreur: Division impossible par zero")
    elif operator == "+":
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "%":
        return(num1 +(num1 * num2 / 100))
    else:
        return("Erreur: Opérateur inconnu")

print(calcule(15, "*", 3))  
print(calcule(10, "/", 0))  
print(calcule(50, "%", 10)) 
print(calcule(20, "/", 2))  