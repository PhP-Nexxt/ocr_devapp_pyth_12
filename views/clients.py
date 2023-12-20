from controllers.validators import str_input, int_input, email_input
from rich.console import Console
from rich.table import Table


class ClientView:
    def __init__(self):
        pass
    
    def clients_menu(self):
        print()
        print("1. Creer un nouveau client : ")
        print("2. Afficher la liste des clients : ")
        print("3. Modifier un client : ")
        print("4. Retourner au menu principal : ")
        return int_input("")
    
    def get_client_data(self):
        full_name = str_input("full name : " )
        email = email_input("email : " )
        phone_number = str_input("phone number : " )
        company_name = str_input("company : " )
        return full_name, email, phone_number, company_name
    
    def display_clients(self, clients):
        table = Table(title="Client List") # Affichage Tableau
        table.add_column("Id", style="white")
        table.add_column("Full Name", style="white")
        table.add_column("Email", style="white")
        table.add_column("Phone number", style="white")
        table.add_column("Company Name", style="white")
        table.add_column("Commercial", style="white")
        for client in clients:
            table.add_row(str(client.id), client.full_name, client.email, client.phone_number ,client.company_name, client.commercial.name)
        console = Console()
        console.print(table) 
        
        # for client in clients:
            # print(client.id, client.full_name)
            
    def get_client_id(self):
        choice = int_input("Entrez identifiant du client concerné : ")
        return choice
    
    def get_update_client(self, client):
        print("tapez Entre pour conserver la valeur sans modification")
        full_name = str_input(f"full name ({client.full_name}) : ", updated=True) or client.full_name
        email = email_input(f"email ({client.email}) : ", updated=True) or client.email
        phone_number = str_input(f"phone number ({client.phone_number}) : ", updated=True ) or client.phone_number
        company_name = str_input(f"company ({client.company_name}) : ", updated=True ) or client.company_name
        return full_name, email, phone_number, company_name
    
    
    
    
        
    