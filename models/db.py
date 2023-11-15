from sqlalchemy import create_engine #Connexion avec DB
from sqlalchemy.orm import sessionmaker # Permet de creer une instance de session

# Code standard pour se connecter a une base de donnée postgre
engine = create_engine("postgresql+psycopg2://epic_event_user:12345678@localhost:5432/epic_event_db", echo=False)
# engine = create_engine("sqlite:///db.sqlite")
conn = engine.connect() 

Session = sessionmaker(bind=engine)

# Créez une instance de session
session = Session()