import statistics

# Demander à l'utilisateur d'entrer deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calculer la somme des deux nombres
somme = nombre1 + nombre2

# Calculer la moyenne des deux nombres
moyenne = (nombre1 + nombre2) / 2

# Calculer l'écart-type des deux nombres
ecart_type = statistics.stdev([nombre1, nombre2])

# Calculer la médiane des deux nombres
liste = [nombre1, nombre2]
liste.sort()
if len(liste) % 2 == 0:
    medianne = (liste[len(liste)//2] + liste[len(liste)//2-1]) / 2
else:
    medianne = liste[len(liste)//2]

# Afficher les résultats
print("La somme des deux nombres est : ", somme)
print("La moyenne des deux nombres est : ", moyenne)
print("L'écart-type des deux nombres est : ", ecart_type)
print("La médiane des deux nombres est : ", medianne)
