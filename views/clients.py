from controllers.validators import str_input, int_input

class ClientView:
    def __init__(self):
        pass
    
    def clients_menu(self):
        print("1. Creer un nouveau client : ")
        print("2. Afficher la liste des clients : ")
        print("3. Modifier un client : ")
        print("4. Retourner au menu principal : ")
        return int_input("")
    
    def get_client_data(self):
        full_name = int_input("full name : " )
        email = input("email : " )
        phone_number = input("phone number : " )
        company_name = int_input("company : " )
        return full_name, email, phone_number, company_name
    
    def display_clients(self, clients):
        for client in clients:
            print(client.id, client.full_name)
            
    def get_client_id(self):
        choice = int(input("Entrez identifiant du client concerné : "))
        return choice
    
    def get_update_client(self, client):
        print("tapez Entre pour conserver la valeur sans modification")
        full_name = str_input(f"full name ({client.full_name}) : ", updated=True) or client.full_name
        email = input(f"email ({client.email}) : " ) or client.email
        phone_number = input(f"phone number ({client.phone_number}) : " ) or client.phone_number
        company_name = str_input(f"company ({client.company_name}) : ", updated=True ) or client.company_name
        return full_name, email, phone_number, company_name
    
    
    
    
        
    