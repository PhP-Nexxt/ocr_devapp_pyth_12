from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) #nullable = valeur recquise
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    password = Column(String, nullable=False)

meta_base = Base.metadata # variable qui permet d'exporter l'ensemble des models Se met a la fin du fichier model
    
    