from .auth import login, logout, create_user
from .contrats import create_contrat, create_event
from views.menu import app_menu
from .clients import ClientControler
from views.clients import ClientView 

class MainController:
    def __init__(self):
        self.client_view = ClientView()
        self.client_controller = ClientControler()
        
    def start(self):
        choice = app_menu() # Appel au menu de view
        if choice == 1:
            login()
        elif choice == 2:
            create_user()
        elif choice == 3:
            self.clients_menu()
        elif choice == 4:
            create_contrat()
        elif choice == 5:
            create_event()
        elif choice == 6:
            logout()
        else:
            print("Choix incorect !")
            
    def clients_menu(self):
        choice = self.client_view.clients_menu()
        if choice == 1:
            self.client_controller.create_client()
        elif choice == 2:
            self.client_controller.display_clients()
        elif choice == 3:
            print("Modifier un client")
        elif choice == 4:
            print("Supprimer un client")
        elif choice == 5:
            self.start()
        
