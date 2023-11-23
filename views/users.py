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

def get_client_data():
    full_name = input("full name : " )
    email = input("email : " )
    phone_number = input("phone number : " )
    company_name = input("company : " )
    return full_name, email, phone_number, company_name

def get_contrat_data():
    client_id = input("Entrez Id du client : " )
    commercial_id = input("Entrez Id du commercial : " )
    amount = input("Montant du contrat : " )
    rest_amount = input("Reste a payer du contrat : " )
    return client_id, commercial_id, amount, rest_amount

def get_event_data():
    name = input("Entrez le nom de l'evenement : ")
    contrat_id = input("Entrez Id du commercial : " )
    client_id = input("Entrez Id du client : " )
    support_id = input("Entrez Id du support : ")
    location = input("Entrez adresse de l'evenement : ")
    attendees = input("Nombre d'invités : ")
    notes = input("Entrez vos notes : ")
    return name, contrat_id, client_id, support_id, location, attendees, notes
    
    
    