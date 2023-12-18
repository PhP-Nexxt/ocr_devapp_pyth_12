from models.db import session
from sqlalchemy.exc import SQLAlchemyError
import sentry_sdk
from models.models import Contrat, RoleEnum
from views.contrats import ContratView
from views.menu import print_message
from .auth import Auth
from .utils import login_required, gestion_or_commercial_required

class ContratsControllers:
    def __init__(self):
        self.contrat_view = ContratView()
        self.auth = Auth()
    
    @login_required
    @gestion_or_commercial_required
    def create_contrat(self):
        current_user = self.auth.get_current_user()
        commercial_id = current_user.id
        # Creation du contrat  
        client_id, amount, rest_amount = self.contrat_view.get_contrat_data()
        new_contrat = Contrat(client_id=client_id, commercial_id=commercial_id, amount=amount, rest_amount=rest_amount)
        session.add(new_contrat)
        try:
            session.commit()
            print_message("Le contrat a été crée")
        except SQLAlchemyError as e:
            sentry_sdk.capture_exception(e)
            print_message("Le contrat n'a pas pu etre crée", error=True)
    
    @login_required
    # Test Sentry    
    def display_contrats(self):
        try:
            contrats = session.query(Contrat).all()
            self.contrat_view.display_contrats(contrats) # Recupere les contrats pour la view
        except Exception as e: # Sentry
            sentry_sdk.capture_exception(e)
            print_message("Erreur d'affichage", error=True)
        
        
    @login_required
    @gestion_or_commercial_required    
    def display_no_signed_contrats(self):
        current_user = self.auth.get_current_user()
        if current_user.role==RoleEnum.COMMERCIAL.value:
            contrats = session.query(Contrat).filter_by(commercial_id=current_user.id, status = False) # Si commercial on recupere les contrat non signés qui le concerne
        else:
            contrats = session.query(Contrat).filter_by(status = False) # Ici on récupere l'ensemble des contrats non signés
        if contrats.count()>0: # Verifie si contrats existent
            self.contrat_view.display_contrats(contrats) # Recupere les contrats pour la view
            return True # On prepare l'info
        else:
            return False
    
    @login_required
    @gestion_or_commercial_required
    def update_contrat(self):
        contrat_exist = self.display_no_signed_contrats() # Appel affichage contrats non signés
        if contrat_exist:
            contrat_id = self.contrat_view.get_contrat_id() # On recupere le choix a modifier via id du client
            contrat = session.query(Contrat).filter_by(id=contrat_id).first()
            rest_amount, status = self.contrat_view.get_update_contrat(contrat)
            contrat.rest_amount = rest_amount
            contrat.status = status
            try:
                session.commit() # Update Database
                print_message("Le contrat a été mis a jour")
            except SQLAlchemyError as e:
                sentry_sdk.capture_exception(e)
                print_message("Le contrat n'a pas pu etre mis a jour", error=True)
        else:
            print("Aucun contrat trouvé ")

    