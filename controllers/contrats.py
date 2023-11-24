from models.db import session
from models.models import Client, Contrat, Event, RoleEnum
from views.users import get_contrat_data, get_event_data
from .auth import load_login_session


def create_contrat():
    # Creation du contrat  
    client_id, commercial_id, amount, rest_amount = get_contrat_data()
    new_contrat = Contrat(client_id=client_id, commercial_id=commercial_id, amount=amount, rest_amount=rest_amount)
    session.add(new_contrat)
    session.commit()

def create_event():
    # Creation evenement
    name, contrat_id, client_id, support_id, location, attendees, notes = get_event_data()
    new_event = Event(name=name, contrat_id=contrat_id, client_id=client_id, support_id=support_id, location=location, attendees=attendees, notes=notes)
    session.add(new_event)
    session.commit()
    
