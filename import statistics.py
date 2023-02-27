import statistics

# Demander à l'utilisateur d'entrer deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisieme nombre : "))
# Calculer la somme des deux nombres
somme = nombre1 + nombre2 + nombre3

# Calculer la moyenne des deux nombres
moyenne = (nombre1 + nombre2) / 2

# Calculer l'écart-type des deux nombres
ecart_type = statistics.stdev([nombre1, nombre2, nombre3])

# Calculer la médiane des deux nombres
liste = [nombre1, nombre2, nombre3]
liste.sort()
if len(liste) % 2 == 0:
    medianne = (liste[len(liste)//3] + liste[len(liste)//3-1]) / 3
else:
    medianne = liste[len(liste)//3]

# Afficher les résultats
print("La somme des trois nombres est : ", somme)
print("La moyenne des trois nombres est : ", moyenne)
print("L'écart-type des trois nombres est : ", ecart_type)
print("La médiane des trois nombres est : ", medianne)
