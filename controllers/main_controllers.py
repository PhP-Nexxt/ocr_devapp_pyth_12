from .auth import login, logout, create_user
from .contrats import create_client, create_contrat, create_event
from views.menu import app_menu


def start():
    choice = app_menu() # Appel au menu de view
    if choice == 1:
        login()
    elif choice == 2:
        create_user()
    elif choice == 3:
        create_client()
    elif choice == 4:
        create_contrat()
    elif choice == 5:
        create_event()
    elif choice == 6:
        logout()
    else:
        print("Choix incorect !")