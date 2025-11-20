phrase = "Bonjour je suis vivant et je m'appelle olivier i"

##################################################################3 Ex 1
def lenght(x):
    count = 0
    for i in x:
        count += 1

    return count

def count_word(x):
    liste_mot = x.split(" ")
    return lenght(liste_mot)

def triage(liste):
    longeur = lenght(liste)

    for i in range(longeur):
        trier = False

        for j in range(0, longeur-i-1):

            if lenght(liste[j]) > lenght(liste[j+1]):
                liste[j],liste[j+1] = liste[j+1], liste[j]
                trier = True
        if trier == False:
            break

    return liste
        

def mot_court_3(x):
    liste_mot = x.split(" ")
    liste_trier = triage(liste_mot)
    liste3 = liste_trier[:3:]
    return liste3

def mot_long_3(x):
    liste_mot = x.split(" ")
    liste_trier = triage(liste_mot)
    liste3 = liste_trier[:lenght(liste_mot)-4:-1]
    return liste3

def texte_inverse(liste):
    liste_mot = liste.split(" ")
    liste_inverse = liste_mot[::-1]
    return " ".join(liste_inverse)

def contient(liste, element):
    for item in liste:
        if item.lower() == element.lower():
            return True
    return False

def texte_unique(texte):
    liste_mot = texte.split(" ")
    uniques = []
    for i in liste_mot:
        if not contient(uniques, i):
            uniques.append(i)
    return " ".join(uniques)



def ex1():
        texte = (input("Entrer votre texte : "))
        print("Choissiser votre modificateur: (1-6)")
        print("1. Afficher le nombre de mot dans votre texte")
        print("2. Afficher les 3 mots les plus courts")
        print("3. Afficher les 3 mots les plus longs")
        print("4. Afficher le texte unique")
        print("5. Afficher le texte inverse")
        print("6. Changer le texte")
        print("7. Quitter au menu principal")

        running_ex1 = True
        while running_ex1 == True:

            choix_ex1 = int(input("Choix: "))
            
            if choix_ex1 == 1:
                print(f"Il y a {count_word(texte)} mots")
            
            if choix_ex1 == 2:
                print(f"Les trois mots les plus courts son: {mot_court_3(texte)}")

            if choix_ex1 == 3:
                print(f"Les trois mots les plus longs son: {mot_long_3(texte)}")

            if choix_ex1 == 4:
                print(f"Texte unique : {texte_unique(texte)}")
            
            if choix_ex1 == 5:
                print(f"Texte inverse : {texte_inverse(texte)}")
            
            if choix_ex1 == 6:
                texte = (input("Entrer votre texte : "))
            
            if choix_ex1 == 7:
                running_ex1 = False
                choix_menu = 0
               
#######################################################################################
###Tableau de selection################################################################

running_main = True
while running_main == True:
    print("Bienvenu Selectionner l'exercice (1-4)")
    print("1. Exercice 1")
    print("2. Exercice 2")
    print("3. Exercice 3")
    print("4. Quitter")
    choix_menu = (input("Choix : "))

    if choix_menu == "1":
        ex1()

    if choix_menu == "2":
        pass
    if choix_menu == "3":
        pass
    if choix_menu == "4":
        print("Au revoir!")
        running_main = False
    else:
        continue

    ########################################################################################################

    #Ex2

    
        


               


        



        
        
        
                        


            
            













        
        
        


