from sqlalchemy.orm.exc import NoResultFound
from models.db import session
from models.models import User
from views.users import get_user_data, get_user_login_data

def create_user():
    # Creation du user en recuperant les valeurs input de views.users.py
    name, lastname, role, password = get_user_data()
    new_user = User(name=name, lastname=lastname,role=role, password=password)
    new_user.set_password(password)
    session.add(new_user)
    session.commit()
    
def login():
    name, password = get_user_login_data()
    try:
        user = session.query(User).filter_by(name=name).one()
        if user.check_password(password):
            print("User exist")
        else:
            print("Invalid password !")
    except NoResultFound:
        print("User does not exist !")
 
def start():
    # create_user()
    login()