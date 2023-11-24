from models.db import session
from models.models import Client, Contrat, Event, RoleEnum
from views.clients import ClientView
from .auth import load_login_session

class ClientControler:
    def __init__(self):
        self.client_view = ClientView()
        
    def create_client(self):
        current_user = load_login_session()
        # Verification du log et du role
        if current_user:
            # Verification du role commercial
            if current_user.role==RoleEnum.COMMERCIAL.value:
                # Creation du client  
                full_name, email, phone_number, company_name = self.client_view.get_client_data()
                # Appel du commercial
                commercial_id = current_user.id
                new_client = Client(full_name=full_name, email=email, phone_number=phone_number, company_name=company_name, commercial_id=commercial_id)
                session.add(new_client)
                session.commit()
            else:
                print("Vous n'etes pas commercial ")
        else:
            print("Vous n'etes pas authentifié ")
            
    def display_clients(self):
        current_user = load_login_session()
        clients = session.query(Client).filter_by(commercial_id=current_user.id)
        for client in clients:
            print(client.full_name)
    

