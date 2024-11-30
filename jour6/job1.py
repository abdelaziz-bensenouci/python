def rectangle(width, height):
    print("|" + "-" * (width - 2) + "|")
    
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    
    print("|" + "-" * (width - 2) + "|")

rectangle(10, 3)


