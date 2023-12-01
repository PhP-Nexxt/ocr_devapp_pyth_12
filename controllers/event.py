from models.db import session
from models.models import Client, Contrat, Event, RoleEnum
from .auth import Auth
from views.event import EventView

class EventController:
    def __init__(self):
        self.event_view = EventView()
        self.auth = Auth()

    def create_event(self):
        # Creation evenement
        name, contrat_id, location, attendees, notes = self.event_view.get_event_data()
        contrat = session.query(Contrat).filter_by(id=contrat_id).first()
        new_event = Event(name=name, contrat_id=contrat_id, client_id=contrat.client_id, location=location, attendees=attendees, notes=notes)
        session.add(new_event)
        session.commit()
        
    def display_event(self):
        current_user = self.auth.load_login_session()
        events = session.query(Event).all()
        self.event_view.display_event(events) # Recupere les events pour la view
        
    def assign_user_support_to_event(self):
        self.display_event() # Appel affichage
        event_id = self.event_view.get_event_id() # On recupere le choix a modifier via id de l'event
        event = session.query(Event).filter_by(id=event_id).first()
        support_id = self.event_view.get_event_support_id()
        event.support_id = support_id
        session.commit() # Maj base de donnée events
        
    def update_event(self):
        self.display_event() # Appel affichage
        event_id = self.event_view.get_event_id() # On recupere le choix a modifier via id du client
        event = session.query(Event).filter_by(id=event_id).first()
        name, location, attendees, start_at, end_at, notes = self.event_view.get_update_event(event)
        event.name = name
        event.location = location
        event.attendees = attendees
        event.start_at = start_at
        event.end_at = end_at
        event.notes = notes
        session.commit() # Maj base de donnée clients
