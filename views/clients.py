

class ClientView:
    def __init__(self):
        pass
    
    def clients_menu(self):
        print("1. Creer un nouveau client : ")
        print("2. Afficher la liste des clients : ")
        print("3. Modifier un client : ")
        print("4. Retourner au menu principal : ")
        return int(input())
    
    def get_client_data(self):
        full_name = input("full name : " )
        email = input("email : " )
        phone_number = input("phone number : " )
        company_name = input("company : " )
        return full_name, email, phone_number, company_name
    
    def display_clients(self, clients):
        for client in clients:
            print(client.id, client.full_name)
            
    def get_client_id(self):
        choice = int(input("Entrez identifiant du client concerné : "))
        return choice
    
    def get_update_client(self, client):
        print("tapez Entre pour conserver la valeur sans modification")
        full_name = input(f"full name ({client.full_name}) : " ) or client.full_name
        email = input(f"email ({client.email}) : " ) or client.email
        phone_number = input(f"phone number ({client.phone_number}) : " ) or client.phone_number
        company_name = input(f"company ({client.company_name}) : " ) or client.company_name
        return full_name, email, phone_number, company_name
    
    
    
    
        
    