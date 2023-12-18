from models.db import session
from sqlalchemy.exc import SQLAlchemyError
import sentry_sdk
from models.models import Contrat, Event
from .auth import Auth
from views.event import EventView
from views.menu import print_message
from .utils import login_required, gestion_required, commercial_required, support_required

class EventController:
    def __init__(self):
        self.event_view = EventView()
        self.auth = Auth()

    @login_required
    @commercial_required
    def create_event(self):
        # Creation evenement
        name, contrat_id, location, attendees, notes = self.event_view.get_event_data()
        contrat = session.query(Contrat).filter_by(id=contrat_id).first()
        new_event = Event(name=name, contrat_id=contrat_id, client_id=contrat.client_id, location=location, attendees=attendees, notes=notes)
        session.add(new_event)
        try:
            session.commit() # Update Database
        except SQLAlchemyError as e:
            sentry_sdk.capture_exception(e)
            print_message("L'evenement pas pu etre crée", error=True)
    
    @login_required    
    def display_event(self):
        events = session.query(Event).all()
        self.event_view.display_event(events) # Recupere les events pour la view
        
    @login_required    
    def display_event_no_support(self):
        events = session.query(Event).filter_by(support_id = None) # Recupere les evenements non attribués
        if events.count()>0: # Verification de la presence d'events non attribués
            self.event_view.display_event(events) # Recupere les events pour la view
            return True
        else:
            return False
    
    @login_required
    @gestion_required    
    def assign_user_support_to_event(self):
        event_exist = self.display_event_no_support() # Appel affichage event non attribués
        if event_exist:
            event_id = self.event_view.get_event_id() # On recupere le choix a modifier via id de l'event
            event = session.query(Event).filter_by(id=event_id).first()
            support_id = self.event_view.get_event_support_id()
            event.support_id = support_id
            try:
                session.commit() # Update Database
                print_message("L'evenement a bien été assigné au User")
            except SQLAlchemyError as e:
                sentry_sdk.capture_exception(e)
                print_message("Le user support n'a pas pu etre ajouté", error=True)
        else:
            print(" Aucun evenement trouvé ")
            
    @login_required    
    def display_support_event(self):
        current_user = self.auth.get_current_user()
        events = session.query(Event).filter_by(support_id = current_user.id) # Recupere les evenements attribués au user support
        if events.count()>0: # Verification de la presence d'events non attribués
            self.event_view.display_event(events) # Recupere les events pour la view
            return True
        else:
            return False
    
    @login_required
    @support_required   
    def update_event(self):
        event_exist = self.display_support_event() # Appel affichage
        if event_exist:
            event_id = self.event_view.get_event_id() # On recupere le choix a modifier via id du client
            event = session.query(Event).filter_by(id=event_id).first()
            name, location, attendees, start_at, end_at, notes = self.event_view.get_update_event(event)
            event.name = name
            event.location = location
            event.attendees = attendees
            event.start_at = start_at
            event.end_at = end_at
            event.notes = notes
            try:
                session.commit() # Update Database
                print_message("Evenement mis a jour")
            except SQLAlchemyError as e:
                sentry_sdk.capture_exception(e)
                print_message("L'evenement n'a pas pu etre mis a jour", error=True)
        else:
            print("Aucun évenement trouvé")
        
    
