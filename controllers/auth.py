from sqlalchemy.orm.exc import NoResultFound
from models.db import session
from models.models import User
import pickle, os # PicklE > sauvegarde une cle de session
from views.users import UserView


SESSION_FILE = "session.pkl" #sauvergarde la session sur la machine(pas Cookie)
class Auth:
    
    def __init__(self):
        self.user_view = UserView()
    
    def login(self):
        existed_user = self.load_login_session() # Verification si loggé
        if existed_user:
            print("Vous etes deja loggé")
        else:
            name, password = self.user_view.get_user_login_data() # Si non > demande authetification
            try:
                user = session.query(User).filter_by(name=name).one()
                if user.check_password(password):
                    self.save_login_session(user) #appel de la fonction
                else:
                    print("Invalid password !")
                    return None
            except NoResultFound:
                print("User does not exist !")
                return None

    def logout(self):
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)

    def save_login_session(self, user):
        with open(SESSION_FILE, "wb") as file: # wb ecriture
            pickle.dump(user.id, file) # Sauvegarde user dans la session en cours
        
    def load_login_session(self): # Verifier et Charger si le user auhthentifié 
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
            
