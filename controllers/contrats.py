from models.db import session
from models.models import Contrat, RoleEnum
from views.contrats import ContratView
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
        session.commit()
    
    @login_required    
    def display_contrats(self):
        contrats = session.query(Contrat).all()
        self.contrat_view.display_contrats(contrats) # Recupere les contrats pour la view
        
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
            session.commit() # Maj base de donnée clients
        else:
            print("Aucun contrat trouvé ")

    