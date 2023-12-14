from models.db import engine, session
from models.models import meta_base, User
from controllers.main_controllers import MainController

# Elements de connexions :
# ______________________________
# Epic_event_postgresql
# Pw 12345678
# Port number 5432
# Pw Table Epic Event > 12345678
# bd : epic_event_db
# user : epic_event_user
# ______________________________




if __name__ == "__main__": # A approfondir
    meta_base.create_all(engine) 
    MainController().start() # Appel class MainControleur puis fonction start
    
    
    
    #To Do > Prepa prez 
    # > Reprendre les livrables a fournir + :
    # Journalisation
    # Shema base de données _ Choix Orm lien avec type de base choisie et pourquoi 
    # Lien et explication du code
    # Tableau droit acces selon role avec decorateurs associés
    # Voir Bouclage execution du programme pour ergonomie
    # README à ecrire
    # Conformite = Soutenance Blanche > Architecture / Class / Décorateurs / Orm
    
    