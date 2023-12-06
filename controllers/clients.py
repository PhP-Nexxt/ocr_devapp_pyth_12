from models.db import session
from models.models import Client
from views.clients import ClientView
from .auth import Auth
from .utils import login_required, commercial_required

class ClientControler:
    def __init__(self):
        self.client_view = ClientView()
        self.auth = Auth()
    
    @login_required
    @commercial_required # Appel au decorateur   
    def create_client(self):
        current_user = self.auth.get_current_user() 
        # Creation du client  
        full_name, email, phone_number, company_name = self.client_view.get_client_data()
        # Appel du commercial
        commercial_id = current_user.id
        new_client = Client(full_name=full_name, email=email, phone_number=phone_number, company_name=company_name, commercial_id=commercial_id)
        session.add(new_client)
        session.commit()
    
    
    @login_required # Appel decorateur     
    def display_clients(self):
        clients = session.query(Client).all()
        self.client_view.display_clients(clients) # Recupere les clients pour la view
        
    @login_required # Appel decorateur     
    def display_commercial_clients(self):
        current_user = self.auth.get_current_user()
        clients = session.query(Client).filter_by(commercial_id=current_user.id)
        if clients.count() > 0:
            self.client_view.display_clients(clients) # Recupere les clients pour la view
            return True
        else:
            return False

    @login_required
    @commercial_required
    def update_clients(self):
        client_exist = self.display_commercial_clients() # Appel affichage
        if client_exist:
            client_id = self.client_view.get_client_id() # On recupere le choix a modifier via id du client
            client = session.query(Client).filter_by(id=client_id).first()
            full_name, email, phone_number, company_name = self.client_view.get_update_client(client)
            client.full_name = full_name
            client.email = email
            client.phone_number = phone_number
            client.company_name = company_name
            session.commit() # Maj base de donnée clients
        else:
            print("Aucun client trouvé")
    