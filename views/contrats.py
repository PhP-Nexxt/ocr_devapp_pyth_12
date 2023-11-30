

class ContratView:
    def __init__(self):
        pass
    
    def contrat_menu(self):
        print("1. Creer un nouveau contrat : ")
        print("2. Afficher la liste des contrats : ")
        print("3. Modifier un contrat : ")
        print("4. Retourner au menu principal : ")
        return int(input())
    
    def get_contrat_data(self):
        client_id = input("Entrez Id du client : " )
        amount = input("Montant du contrat : " )
        rest_amount = input("Reste a payer du contrat : " )
        return client_id, amount, rest_amount
    
    def display_contrats(self,contrats):
        for contrat in contrats:
            print(contrat.id, contrat.amount, contrat.client.full_name)
        
    def get_contrat_id(self):
        choice = int(input("Entrez identifiant du contrat concerné : "))
        return choice
    
    def get_update_contrat(self, contrat):
        print("tapez Entre pour conserver la valeur sans modification")
        rest_amount = input(f"Reste a payer du contrat ({contrat.rest_amount}): " ) or contrat.rest_amount
        status_choice = input("Voulez-vous valider la signature du contrat ?\n1. Oui \n2. Non \n")
        status = True if status_choice == "1" else False 
        return rest_amount, status 
    