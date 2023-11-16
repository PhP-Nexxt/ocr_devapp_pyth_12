from sqlalchemy.orm.exc import NoResultFound
from models.db import session
from models.models import User, Client
from views.users import get_user_data, get_user_login_data, get_client_data

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
        
def create_client():
    # Creation du client  
    full_name, email, phone_number, company_name, commercial_id = get_client_data()
    new_client = Client(full_name=full_name, email=email, phone_number=phone_number, company_name=company_name, commercial_id=commercial_id)
    session.add(new_client)
    session.commit()
 
def start():
    # create_user()
    # login()
    create_client()