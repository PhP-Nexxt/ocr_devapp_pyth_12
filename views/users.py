from models.models import RoleEnum
from controllers.validators import str_input, int_input
from rich.console import Console
from rich.table import Table

class UserView:

    def __init__(self):
        pass
    
    def user_menu(self):
        print("1. Creer un utilisateur : ")
        print("2. Afficher la liste des utilisateurs : ")
        print("3. Modifier un utilisateur : ")
        print("4. Supprimer un utilisateur : ")
        print("5. Retourner au menu principal : ")
        return int_input("")
    
    def get_user_data(self):
        # Formulaire de saisie puis creation dans controllers.users.py
        name = str_input("Entrez votre Prenom : ") # Lien avec validators
        lastname = str_input("Entrez votre nom : ")
        print()
        role_list = [e.value for e in RoleEnum]
        for key, role in enumerate(role_list): # key = position dans la liste
            print(key+1, role) # Recupere le role de RoleEnum en partant de 1
        choice = int_input("Entrez votre role parmis le choix ci-dessus : ")
        while choice not in [key+1 for key, role in enumerate(role_list)]: # Verification des roles contenus dans RoleEnum
            choice = int_input("Entrez un role valide : ")
        role = role_list[choice-1] # Rectification de l'affichage (+1)
        password = str_input("Entrez votre Pw : ")
        return name, lastname, role, password

    def get_user_login_data(self):
        # Ici on recupere les informations d'identification du user (formulaire)
        name = str_input("Entrez votre nom : " )
        password = str_input("Entrez votre Pw : ")
        return name, password
    
    def display_user(self, users):
        table = Table(title="User List") # Affichage Tableau
        table.add_column("Id", style="magenta")
        table.add_column("Name", style="magenta")
        table.add_column("Last Name", style="magenta")
        table.add_column("Role", style="magenta")
        for user in users:
            table.add_row(str(user.id), user.name, user.lastname, user.role)
        console = Console()
        console.print(table) 
           
    def get_user_id(self):
        choice = int_input("Entrez identifiant du user concerné : ")
        return choice
    
    def get_update_user(self, user):
        print("tapez Entre pour conserver la valeur sans modification")
        name = str_input(f"name ({user.name}) : ", updated=True ) or user.name
        lastname = str_input(f"lastname ({user.lastname}) : ", updated=True) or user.lastname
        password = str_input("Password (******) : ", updated=True)
        print()
        role_list = [e.value for e in RoleEnum]
        for key, role in enumerate(role_list): # key = position dans la liste
            print(key+1, role) # Recupere le role de RoleEnum en partant de 1
        choice = int_input(f"Entrez votre role parmis le choix ci-dessus ({user.role}): ", updated=True)
        while choice and choice not in [key+1 for key, role in enumerate(role_list)]: # Verification des roles contenus dans RoleEnum + rentre dans le role si user a saisie une valeur
            choice = int_input("Entrez un role valide : ", updated=True)
        if choice:
            role = role_list[choice-1] # Rectification de l'affichage (+1)
        else:
            role = user.role
        return name, lastname, password, role
    
    
    