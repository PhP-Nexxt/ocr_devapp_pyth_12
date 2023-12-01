from models.models import RoleEnum

class UserView:

    def __init__(self):
        pass
    
    def user_menu(self):
        print("1. Creer un utilisateur : ")
        print("2. Afficher la liste des utilisateurs : ")
        print("3. Modifier un utilisateur : ")
        print("4. Supprimer un utilisateur : ")
        print("5. Retourner au menu principal : ")
        return int(input())
    
    def get_user_data(self):
        # Formulaire de saisie puis creation dans controllers.users.py
        name = input("Entrez votre Prenom : ")
        lastname = input("Entrez votre nom : ")
        print()
        role_list = [e.value for e in RoleEnum]
        for key, role in enumerate(role_list): # key = position dans la liste
            print(key+1, role) # Recupere le role de RoleEnum en partant de 1
        choice = int(input("Entrez votre role parmis le choix ci-dessus : "))
        while choice not in [key+1 for key, role in enumerate(role_list)]: # Verification des roles contenus dans RoleEnum
            choice = input("Entrez un role valide : ")
        role = role_list[choice-1] # Rectification de l'affichage (+1)
        password = input("Entrez votre Pw : ")
        return name, lastname, role, password

    def get_user_login_data(self):
        # Ici on recupere les informations d'dentification du user (formulaire)
        name = input("Entrez votre nom : " )
        password = input("Entrez votre Pw : ")
        return name, password
    
    
    
    