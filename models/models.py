from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) #nullable = valeur recquise
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    def set_password(self, password): 
        # Hachez le mot de passe avec bcrypt avant de le stocker
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        # Vérifiez si le mot de passe correspond au hachage stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

meta_base = Base.metadata # variable qui permet d'exporter l'ensemble des models Se met a la fin du fichier model
    
    