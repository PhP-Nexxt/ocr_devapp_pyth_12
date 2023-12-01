from sqlalchemy.orm.exc import NoResultFound
from models.db import session
from models.models import User
import pickle, os # PicklE > sauvegarde une cle de session
from views.users import UserView


class UserController:
    def __init__(self):
        self.user_view = UserView()

    def create_user(self):
        # Creation du user en recuperant les valeurs input de views.users.py
        name, lastname, role, password = self.user_view.get_user_data()
        new_user = User(name=name, lastname=lastname,role=role, password=password)
        new_user.set_password(password)
        session.add(new_user)
        session.commit()

