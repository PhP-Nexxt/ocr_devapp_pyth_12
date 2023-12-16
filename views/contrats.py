from controllers.validators import str_input, int_input
from rich.console import Console
from rich.table import Table


class ContratView:
    def __init__(self):
        pass
    
    def contrat_menu(self):
        print("1. Creer un nouveau contrat : ")
        print("2. Afficher la liste des contrats : ")
        print("3. Modifier un contrat : ")
        print("4. Retourner au menu principal : ")
        return int_input("")
    
    def get_contrat_data(self):
        client_id = int_input("Entrez Id du client : " )
        amount = int_input("Montant du contrat : " )
        rest_amount = int_input("Reste a payer du contrat : " )
        return client_id, amount, rest_amount
    
    def display_contrats(self,contrats):
        table = Table(title="Contrat List") # Affichage Tableau
        table.add_column("Id", style="magenta")
        table.add_column("Amount", style="magenta")
        table.add_column("Name", style="magenta")
        for contrat in contrats:
            table.add_row(str(contrat.id), str(contrat.amount), contrat.client.full_name)
        console = Console()
        console.print(table) 
        
        #for contrat in contrats:
            #print(contrat.id, contrat.amount, contrat.client.full_name)
        
    def get_contrat_id(self):
        choice = int_input("Entrez identifiant du contrat concerné : ")
        return choice
    
    def get_update_contrat(self, contrat):
        print("tapez Entre pour conserver la valeur sans modification")
        rest_amount = int_input(f"Reste a payer du contrat ({contrat.rest_amount}): ", updated=True ) or contrat.rest_amount
        status_choice = int_input("Voulez-vous valider la signature du contrat ?\n1. Oui \n2. Non \n")
        status = True if status_choice == 1 else False 
        return rest_amount, status 
    