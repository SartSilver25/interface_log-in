nom = input("Entrer votre nom : ")
age = input("Entrer votre age : ")
taille = input("Entrer votre taille : ")

liste1 = input("Entrer votre fruit prefere : ")
liste2 = input("Entrer votre deuxieme fruit prefere : ")
liste3 = input("Entrer votre troisieme fruit prefere : ")

nomMaj = nom.upper()

liste = [liste1, liste2, liste3]

print("\nSalutation, ", nomMaj)
print("Age : ", age)
print("Taille : ", taille)
print("Voici vos fruits preferes : ", liste)