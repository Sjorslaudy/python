def quick_sort(sequence): # Maak een functie genaamd "quicksort", en geef hem de variabel "sequence"
    length = len(sequence) # Variabel "length" is de lengte van de variabel "sequence"
    if length <= 1: # Als variabel "lengte" gelijk aan of onder 1 is
        return sequence # Geef het de "sequence"?
    else: # Zo niet
        pivot = sequence.pop() # Maak variabel "pivot" en geef het het voor-laatste getal van "sequence"

    items_greater = [] # Maak list variabel "items_greater"
    items_lower = [] # Maak list variabel "items_lower"
  
    for item in sequence: # Voor de getallen in "sequence"
        if item > pivot: # Als een getal hoger is dan de pivot
            items_greater.append(item) # Voeg dat getal toe aan variabel "items_greater"

        else: # Zo niet
            items_lower.append(item) # Voeg dat getal toe aan variabel "items_lower"

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) # Herhaal de functie "quicksort" voor alles onder de pivot en daarna boven de pivot
output = quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]) # Variabel "output" is de output van functie "quicksort" over gegeven reeks
print(output) #  Print variabel "output" naar de standaard output
