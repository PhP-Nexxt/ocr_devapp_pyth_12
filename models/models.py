from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship
from enum import Enum
import bcrypt

Base = declarative_base()


class RoleEnum(Enum): # Liste de choix du rôle
    COMMERCIAL = "commercial"
    SUPPORT = "support"
    GESTION = "gestion"
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) #nullable = valeur recquise
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    @validates('role') #Verification du rôle
    def validate_role(self, key, role):
        if role not in [e.value for e in RoleEnum]:  
            raise ValueError(f'Invalid role: {role}')
        return role
    
    def set_password(self, password): 
        # Hachez le mot de passe avec bcrypt avant de le stocker
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        # Vérifiez si le mot de passe correspond au hachage stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False) #nullable = valeur recquise
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now) # Prend la date actuelle
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) # Prend la date de la derniere update
    commercial = relationship("User") # Lien avec la classe User
    commercial_id = Column(Integer, ForeignKey("user.id")) # Ref a la table user
    
    


meta_base = Base.metadata # variable qui permet d'exporter l'ensemble des models Se met a la fin du fichier model
    
    