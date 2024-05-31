def canIBuyBeer(age, location):
    if age >= 18 and location == "krogen":
        return True
    if age >= 20 and location == "systemet":
        return True    
    return False

# A arrange
# A act - anropar
# A assert - vi verifierar

# med enhetstester vill vi fånmga sk sidoeffekter

# while True:
#     age = int(input("Age"))
#     loc = input("Var är du")
#     c = canIBuyBeer(age,loc)
#     if c == True:
#         print("Yep")
#     else:
#         print("No")
