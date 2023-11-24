from models.db import engine, session
from models.models import meta_base, User
from controllers.main_controllers import MainController

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