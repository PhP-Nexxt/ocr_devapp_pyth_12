from controllers.validators import str_input, int_input

class EventView:
    def __init__(self):
        pass
    
    def event_menu(self):
        print("1. Créer un nouvel évenement : ")
        print("2. Afficher la liste des évenements : ")
        print("3. Modifier un évenement : ")
        print("4. Assigner un user support à un evenement : ")
        print("5. Retourner au menu principal : ")
        return int_input("")
    
    def get_event_data(self):
        name = str_input("Entrez le nom de l'evenement : ")
        contrat_id = input("Entrez Id du contrat : " )
        location = str_input("Entrez adresse de l'evenement : ")
        attendees = int_input("Nombre d'invités : ")
        notes = str_input("Entrez vos notes : ")
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
    
    def get_update_event(self, event):
        print("tapez Entre pour conserver la valeur sans modification")
        name = str_input(f"Nom de l'evenement ({event.name}): ", updated=True) or event.name
        location = str_input(f"Lieu de l'evenement ({event.location}): ", updated=True) or event.location
        attendees = int_input(f"Nombre de participants ({event.attendees}): ", updated=True) or event.attendees
        start_at = input(f"Date de debut ({event.start_at}): ") or event.start_at
        end_at = input(f"Date de fin ({event.end_at}): ") or event.end_at
        notes = str_input(f"Notes ({event.notes}): ", updated=True) or event.notes
        return name, location, attendees, start_at, end_at, notes