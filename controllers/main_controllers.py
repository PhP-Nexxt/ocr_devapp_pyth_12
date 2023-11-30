from .auth import login, logout, create_user
from views.menu import app_menu
from .clients import ClientControler
from .contrats import ContratsControllers
from .event import EventController
from views.clients import ClientView 
from views.contrats import ContratView
from views.event import EventView

class MainController:
    def __init__(self):
        self.client_view = ClientView()
        self.contrat_view = ContratView()
        self.event_view = EventView()
        self.client_controller = ClientControler()
        self.contrat_controller = ContratsControllers()
        self.event_controller = EventController()
        
    def start(self):
        choice = app_menu() # Appel au menu de view
        if choice == 1:
            login()
        elif choice == 2:
            create_user()
        elif choice == 3:
            self.clients_menu()
        elif choice == 4:
            self.contrats_menu()
        elif choice == 5:
            self.event_menu()
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
            self.client_controller.update_clients() # Appel fonction update
        elif choice == 4:
            self.start()
            
    def contrats_menu(self):
        choice = self.contrat_view.contrat_menu()
        if choice == 1:
            self.contrat_controller.create_contrat()
        elif choice == 2:
            self.contrat_controller.display_contrats()
        elif choice == 3:
            self.contrat_controller.update_contrat()
        elif choice == 4:
            self.start()
            
    def event_menu(self):
        choice = self.event_view.event_menu()
        if choice == 1:
            self.event_controller.create_event()
        elif choice == 2:
            self.event_controller.display_event()
        elif choice == 3:
            pass
        elif choice == 4:
            self.event_controller.assign_user_support_to_event()
        elif choice == 5:
            self.start()
        
