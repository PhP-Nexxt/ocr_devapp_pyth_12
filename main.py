from db import engine, session
from models import meta_base

















if __name__ == "__main__": # A approfondir
    meta_base.create_all(engine) 