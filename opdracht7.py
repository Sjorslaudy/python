from datetime import date # gebruik pyton's ingebouwde datum/tijd module en import datum.

def age(birthdate): # gebruik functie;leeftijd met variabel birthdate (komt terug in deze functie)
 
    today = date.today() # vanuit de date functie, pak vandaag
    
    # A bool that represents if today's day/month precedes the birth day/month
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))  # check of de huidige dag eerder is dan de verjaardag
    
    # Calculate the difference in years from the date object's components
    year_difference = today.year - birthdate.year # variabel = jaar vandaag - Verjaardag jaar
    
    age = year_difference - one_or_zero   
    
    return age # uitkomst
     


Jaar = int(input("Geboorte jaar?:")) # variabel krijgt inp(getal) --> input(invullen) 
Datum = int(input("Geboorte maand?:"))
Dag = int(input("Geboorte dag?:")) 
print(age(date(Jaar, Datum, Dag)))
Leeftijd = age(date(Jaar, Datum, Dag))



if Leeftijd < 18: # Als leeftijd onder 18 is 
    print("Je bent nog niet oud genoeg om motor te rijden!") # Print dan (je bent nog niet oud genoeg)

else: # Als ouder dan 18 
    print("Je bent oud genoeg om motor te mogen rijden!") # Print dan (je bent oud genoeg om te rijden)
