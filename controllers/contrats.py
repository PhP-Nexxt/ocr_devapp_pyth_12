from models.db import session
from models.models import Client, Contrat, Event, RoleEnum
from views.contrats import ContratView
from .auth import Auth
from sqlalchemy import exc

class ContratsControllers:
    def __init__(self):
        self.contrat_view = ContratView()
        self.auth = Auth()

    def create_contrat(self):
        current_user = self.auth.get_current_user()
        commercial_id = current_user.id
        # Creation du contrat  
        client_id, amount, rest_amount = self.contrat_view.get_contrat_data()
        new_contrat = Contrat(client_id=client_id, commercial_id=commercial_id, amount=amount, rest_amount=rest_amount)
        session.add(new_contrat)
        session.commit()
        
    def display_contrats(self):
        current_user = self.auth.get_current_user()
        contrats = session.query(Contrat).filter_by(commercial_id=current_user.id)
        self.contrat_view.display_contrats(contrats) # Recupere les contrats pour la view

    def update_contrat(self):
        self.display_contrats() # Appel affichage
        contrat_id = self.contrat_view.get_contrat_id() # On recupere le choix a modifier via id du client
        contrat = session.query(Contrat).filter_by(id=contrat_id).first()
        rest_amount, status = self.contrat_view.get_update_contrat(contrat)
        contrat.rest_amount = rest_amount
        contrat.status = status
        session.commit() # Maj base de donnée clients

    