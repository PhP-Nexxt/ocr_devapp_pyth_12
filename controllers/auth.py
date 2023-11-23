from sqlalchemy.orm.exc import NoResultFound
from models.db import session
from models.models import User
import pickle, os # PicklE > sauvegarde une cle de session
from views.users import get_user_data, get_user_login_data

def create_user():
    # Creation du user en recuperant les valeurs input de views.users.py
    name, lastname, role, password = get_user_data()
    new_user = User(name=name, lastname=lastname,role=role, password=password)
    new_user.set_password(password)
    session.add(new_user)
    session.commit()
    
def login():
    existed_user = load_login_session() # Verification si loggé
    if existed_user:
        print("Vous etes deja logger")
    else:
        name, password = get_user_login_data() # Si non > demande authetification
        try:
            user = session.query(User).filter_by(name=name).one()
            if user.check_password(password):
                save_login_session(user) #appel de la fonction
            else:
                print("Invalid password !")
                return None
        except NoResultFound:
            print("User does not exist !")
            return None
        
SESSION_FILE = "session.pkl" #sauvergarde la session sur la machine(pas Cookie)

def logout():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

def save_login_session(user):
    with open(SESSION_FILE, "wb") as file: # wb ecriture
        pickle.dump(user.id, file) # Sauvegarde user dans la session en cours
    
def load_login_session(): # Verifier et Charger si le user auhthentifié 
    try:
        with open(SESSION_FILE, "rb") as file: # rb lecture
            user_id = pickle.load(file) # Lecture contenu du fichier (id)
            if user_id:
                user = session.query(User).filter_by(id=user_id).one()
                return user
            else:
                return None
    except FileNotFoundError:
        return None
        
