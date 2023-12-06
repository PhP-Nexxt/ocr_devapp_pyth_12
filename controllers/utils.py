# Création des decorateurs / Gestion droits 

def login_required(func):
    def inner(self):
        current_user = self.auth.get_current_user()
        # Verification du log et du role
        if current_user:
            result = func(self)
            return result
        else:
            print("Vous n'etes pas authentifié ")
    return inner

def gestion_required(func):
    def inner(self):
        current_user = self.auth.is_gestion()
        # Verification du log et du role gestion
        if current_user:
            result = func(self)
            return result
        else:
            print("Vous n'etes pas Gestionnaire ")
    return inner

def commercial_required(func):
    def inner(self):
        current_user = self.auth.is_commercial()
        # Verification du log et du role commercial
        if current_user:
            result = func(self)
            return result
        else:
            print("Vous n'etes pas Commercial ")
    return inner

def support_required(func):
    def inner(self):
        current_user = self.auth.is_support()
        # Verification du log et du role support
        if current_user:
            result = func(self)
            return result
        else:
            print("Vous n'etes pas de l'équipe support ")
    return inner

def gestion_or_commercial_required(func):
    def inner(self):
        current_user = self.auth.is_commercial_or_gestion()
        # Verification du log et du role support
        if current_user:
            result = func(self)
            return result
        else:
            print("Vous n'etes pas de l'équipe Support ou Commercial")
    return inner