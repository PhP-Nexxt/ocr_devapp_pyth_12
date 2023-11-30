
class EventView:
    def __init__(self):
        pass
    
    def event_menu(self):
        print("1. Créer un nouvel évenement : ")
        print("2. Afficher la liste des évenements : ")
        print("3. Modifier un évenement : ")
        print("4. Assigner un user support à un evenement : ")
        print("5. Retourner au menu principal : ")
        return int(input())
    
    def get_event_data(self):
        name = input("Entrez le nom de l'evenement : ")
        contrat_id = input("Entrez Id du contrat : " )
        location = input("Entrez adresse de l'evenement : ")
        attendees = input("Nombre d'invités : ")
        notes = input("Entrez vos notes : ")
        return name, contrat_id, location, attendees, notes
    
    def display_event(self,events):
        for event in events:
            print(event.id, event.name, event.location, event.attendees)
        
    def get_event_id(self):
        choice = int(input("Entrez identifiant l'evenement concerné : "))
        return choice
    
    def get_event_support_id(self):
        support_id = int(input("Entre l'identifiant du collaborateur support : "))
        return support_id