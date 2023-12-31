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
    import sentry_sdk

    sentry_sdk.init(
        dsn="https://ef07de3146c9d4b7248734c46fff5e11@o4506410812375040.ingest.sentry.io/4506410861461504",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    
    meta_base.create_all(engine) 
    MainController().start() # Appel class MainControleur puis fonction start
