
def get_user_data():
    # Formulaire de saisie puis creation dans controllers.users.py
    name = input("Entrez votre Prenom : ")
    lastname = input("Entrez votre nom : ")
    role = input("Entrez votre role : ")
    password = input("Entrez votre Pw : ")
    return name, lastname, role, password

def get_user_login_data():
    # Ici on recupere les informations d'dentification du user (formulaire)
    name = input("Entrez votre nom : " )
    password = input("Entrez votre Pw : ")
    return name, password