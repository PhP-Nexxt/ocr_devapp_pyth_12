from db import engine, session
from models import meta_base

# Epic_event_postgresql
# Pw 12345678
# Port number 5432
# Pw Table Epic Event > 12345678
# bd : epic_event_db
# user : epic_event_user















if __name__ == "__main__": # A approfondir
    meta_base.create_all(engine) 