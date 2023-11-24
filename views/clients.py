

class ClientView:
    def __init__(self):
        pass
    
    def clients_menu(self):
        print("1. Creer un nouveau client : ")
        print("2. Afficher la liste des clients : ")
        print("3. Modifier un client : ")
        print("4. Supprimer un client : ")
        print("5. Retourner au menu principal : ")
        return int(input())
    
    def get_client_data(self):
        full_name = input("full name : " )
        email = input("email : " )
        phone_number = input("phone number : " )
        company_name = input("company : " )
        return full_name, email, phone_number, company_name
    
    