from controllers.validators import int_input

def app_menu():
    print("1. Se connecter : ")
    print("2. Gestion des utilisateurs : ")
    print("3. Gestion des clients : ")
    print("4. Gestion des contrats : ")
    print("5. Gestion des evenements : ")
    print("6. Se deconnecter : ")
    return int_input("") # Lien avec Validators