def counter():
    total = 0
    while True:
        print("Total: "+ str(total))
        total += int(input("To add: "))
        
counter()
