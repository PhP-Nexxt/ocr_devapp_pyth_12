from models.models import RoleEnum

def get_user_data():
    
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

def get_user_login_data():
    # Ici on recupere les informations d'dentification du user (formulaire)
    name = input("Entrez votre nom : " )
    password = input("Entrez votre Pw : ")
    return name, password
    
    
    