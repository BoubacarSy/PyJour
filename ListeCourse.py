import sys
import json
import os
from textwrap import indent

#Aficher les options
print("Choisissez parmi les 5 options suivantes: ")
print("1. Ajouter un élément à la liste de courses")
print("2. Retirer un élément de la liste de courses")
print("3. Afficher les éléments de la liste de courses")
print("4. Vider la liste de courses")
Courses=[]
CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "course.json")

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        Courses = json.load(f)
else:
    Courses = []

while True:
    choix=input("Votre choix: ")
    while not (choix.isdigit() ):
        print("Choix invalide")
        break
    if choix == "1":
        ajout=input("Ajoutez un element: ")
        Courses.append(ajout)
        print(f"element '{ajout}' ajouté avec succee")
    elif choix=="2":
        retirer=input("Retirez un element: ")
        if retirer in Courses:
            Courses.remove(retirer)
            print("Element retire avec succee")
        else:
            print("Element introuvable")
    elif choix=="3":
        with open("course.json","r") as f:
            liste = json.load(f)
        #for i ,elemnent in enumerate(Courses) :
        print(Courses)
    elif choix=="4":
        Courses.clear()
    elif choix=="5":
        with open(LISTE_PATH,"w") as f:
            json.dump(Courses,f,indent=4)
        print("Au revoir...")
        sys.exit()
