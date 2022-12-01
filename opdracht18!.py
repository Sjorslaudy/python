def factorial(n): # maak functie factorial (getal)

    factorial=1 # zet basis waarde factorial


    for i in range (n): # voer het aantal hele getallen in N 
        factorial*=i+1   # factorial maal de huidige loop + 1


    return factorial # Als functie voltooid is geef de uitkomst

userinput = int(input('voer getal in: ')) # vraag voor getal om voor te berekenen  
print (factorial(userinput)) # run de function en geef de output