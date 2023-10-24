import tkinter as tk

def Valider():
    nom = champ_pseudo.get()
    mdp = champ_mdp.get()
    email = champ_email.get()

    print("['"+ nom +"', '"+ mdp +"', '" + email + "']")

fenetre = tk.Tk()
fenetre.title("Ma Premiere interface graphique")

Label_name = tk.Label(fenetre, text="Nom d'utilisateur")
Label_name.pack()

champ_pseudo = tk.Entry(fenetre)
champ_pseudo.pack()

Label_mdp = tk.Label(fenetre, text="Mot de Passe")
Label_mdp.pack()

champ_mdp = tk.Entry(fenetre, show="*")
champ_mdp.pack()

Label_email = tk.Label(fenetre, text="Adresse Email")
Label_email.pack()

champ_email = tk.Entry(fenetre)
champ_email.pack()

boutonFinish = tk.Button(fenetre, text="Valider l'inscription",command=Valider)
boutonFinish.pack()

fenetre.geometry("400x300")

fenetre.mainloop()
