import random
namn = input("Säg ditt spelar namn --> ")
print(f"Hej {namn}!")
omgångar = int(input("Hur många omgångar? --> "))
val = ["sten","sax","påse"]
forlorar_mot = {
    "sten": "påse",
    "sax": "sten",
    "påse": "sax"
}
poäng = 0
pythonpoäng = 0
for i in range(omgångar):
    print(f"Spelomgång {i+1}: \n-------------")
    välj = input("Välj mellan 'Sten','Sax','Påse'! ---> ")
    lowervälj = välj.lower()
    rannum = random.randint(0,2)
    pythonval = val[rannum]
    print(pythonval)
    if lowervälj == pythonval:
        print("oavgjort!")
    elif lowervälj == forlorar_mot[pythonval]:
        print("Du vann!")
        poäng += 1
    else:
        pythonpoäng += 1
        print("Du förlora!")
print("Python poäng --->",pythonpoäng)
print(namn,"poäng --->",poäng)
    