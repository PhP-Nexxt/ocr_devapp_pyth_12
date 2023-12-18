from sqlalchemy.orm.exc import NoResultFound
import sentry_sdk
from models.db import session
from models.models import User
import pickle, os # PicklE > sauvegarde une cle de session
from views.users import UserView
from views.menu import print_message
from models.models import RoleEnum

SESSION_FILE = "session.pkl" #sauvergarde la session sur la machine(pas Cookie)
class Auth:
    
    def __init__(self):
        self.user_view = UserView()
    
    def login(self):
        existed_user = self.get_current_user() # Verification si loggé
        if existed_user:
            print_message("Vous etes deja loggé")
        else:
            name, password = self.user_view.get_user_login_data() # Si non > demande authetification
            try:
                user = session.query(User).filter_by(name=name).one()
                if user.check_password(password):
                    self.save_login_session(user) #appel de la fonction
                    print_message("You are logged")
                else:
                    print_message("Invalid password !", error=True) # Sortie red
                    return None
            except NoResultFound as e:
                sentry_sdk.capture_exception(e)
                print_message("User does not exist", error=True) # Sortie red
                return None

    def logout(self):
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)

    def save_login_session(self, user):
        with open(SESSION_FILE, "wb") as file: # wb ecriture
            pickle.dump(user.id, file) # Sauvegarde user dans la session en cours
        
    def get_current_user(self): # Verifier et Charger si le user auhthentifié 
        try:
            with open(SESSION_FILE, "rb") as file: # rb lecture
                user_id = pickle.load(file) # Lecture contenu du fichier (id)
                if user_id:
                    user = session.query(User).filter_by(id=user_id).one()
                    return user
                else:
                    return None
        except FileNotFoundError as e:
            sentry_sdk.capture_exception(e)
            return None
    
    # Creation des roles
    def is_commercial(self):
        # Role : Commercial
        current_user = self.get_current_user()
        # Verification du log et du role & # Verification du role commercial
        if current_user and current_user.role==RoleEnum.COMMERCIAL.value:
            return current_user
        return None
        
    def is_gestion(self):
        # Role : Gestion
        current_user = self.get_current_user()
        # Verification du log et du role & # Verification du role commercial
        if current_user and current_user.role==RoleEnum.GESTION.value:
            return current_user
        return None
    
    def is_commercial_or_gestion(self):
        # Role : Gestion & Commercial
        return self.is_commercial() or self.is_gestion()
    
    def is_support(self):
        # Role : Support
        current_user = self.get_current_user()
        # Verification du log et du role & # Verification du role commercial
        if current_user and current_user.role==RoleEnum.SUPPORT.value:
            return current_user
        return None