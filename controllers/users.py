from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from models.db import session
import sentry_sdk
from models.models import User
import pickle, os # PicklE > sauvegarde une cle de session
from views.users import UserView
from views.menu import print_message
from .utils import login_required, gestion_required
from .auth import Auth

class UserController:
    def __init__(self):
        self.user_view = UserView()
        self.auth = Auth()

    @login_required
    @gestion_required
    def create_user(self):
        # Creation du user en recuperant les valeurs input de views.users.py
        name, lastname, role, password = self.user_view.get_user_data()
        new_user = User(name=name, lastname=lastname,role=role, password=password)
        new_user.set_password(password)
        session.add(new_user)
        try:
            session.commit() # Update Database
            print_message("User has been created")
        except SQLAlchemyError as e:
            sentry_sdk.capture_exception(e)
            print_message("User created error", error=True)
        
    @login_required
    @gestion_required
    def display_users(self):
        users = session.query(User).all()
        self.user_view.display_user(users) # Recupere les users pour la view
    
    @login_required
    @gestion_required
    def update_user(self):
        self.display_users() # Appel affichage
        user_id = self.user_view.get_user_id() # On recupere le choix a modifier via id du user
        user = session.query(User).filter_by(id=user_id).first()
        name, lastname, password, role = self.user_view.get_update_user(user)
        user.name = name
        user.lastname = lastname
        user.role = role
        if password: # Si user saisie un PW nouveau > Maj DB sinon rien
            user.password = password
            user.set_password(password)
        try:
            session.commit() # Update Database
            print_message("User has been updated")
        except SQLAlchemyError as e:
            sentry_sdk.capture_exception(e)
            print_message("User updated error", error=True)

    @login_required
    @gestion_required
    def delete_user(self):
        self.display_users() # Appel affichage
        user_id = self.user_view.get_user_id() # On recupere le choix a modifier via id du user
        user = session.query(User).filter_by(id=user_id).first()
        try:
            session.delete(user)
            session.commit()
            print_message("user deleted")
        except SQLAlchemyError as e:
            print("Impossible de supprimer cet utilisateur. Il est associé une ressource : client, contrat, event")
            sentry_sdk.capture_exception(e)
            print_message("Error deleted user", error=True)