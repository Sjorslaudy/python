numbers = str(input("Enter 5 numbers sepperated by spaces: ") or "1 2 3 4 5") # Vraag voor nummers 

numberlist = list(map(int, numbers.split())) # Maak variabel "numberlist" met een lijst van de getallen in "numbers" gesplitsts met de spaties.
numberlist.sort() # Sorteer "numberlist" van klein naar groot

print(numberlist[::-1]) # Draai "numberlist" om van klein naar groot tot groot naar klein