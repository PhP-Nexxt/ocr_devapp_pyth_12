from models.models import RoleEnum

def get_user_data():
    # Formulaire de saisie puis creation dans controllers.users.py
    name = input("Entrez votre Prenom : ")
    lastname = input("Entrez votre nom : ")
    print()
    for role in RoleEnum:
        print(role.value) # Recupere le role de RoleEnum
    role = input("Entrez votre role parmis le choix ci-dessus : ")
    while role not in [role.value for role in RoleEnum]: # Verification des roles contenus dans RoleEnum
        role = input("Entrez un role valide : ")
    
    password = input("Entrez votre Pw : ")
    return name, lastname, role, password

def get_user_login_data():
    # Ici on recupere les informations d'dentification du user (formulaire)
    name = input("Entrez votre nom : " )
    password = input("Entrez votre Pw : ")
    return name, password

def get_client_data():
    full_name = input("full name : " )
    email = input("email : " )
    phone_number = input("phone number : " )
    company_name = input("company : " )
    commercial_id = input("commercial : " )
    return full_name, email, phone_number, company_name, commercial_id