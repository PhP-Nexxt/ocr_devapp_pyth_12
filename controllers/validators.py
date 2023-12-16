import re # Regex > Permet de gerer les validateurs



def str_input(message, updated=False):
    text = input(message)
    pattern = r'^.{3,}$'  # Au moins 3 caractères
    while (not updated or (text and updated)) and not bool(re.match(pattern, text)):
        print("Saisie incorrect, le texte doit contenir au moins 3 caracteres")
        text = input(message)
    return text

def int_input(message, updated=False):
    text = input(message)
    pattern = r'^\d+$'  # Entier positif uniquement
    while (not updated or (text and updated)) and not bool(re.match(pattern, str(text))):
        print("Saisie incorrect, il faut entrer un nombre entier positif")
        text = input(message)
    if text: # Condition si pas entrée = return int
        return int(text)
    else:
        return text

def email_input(message, updated=False):
    text = input(message)
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Format d'une adresse e-mail
    while (not updated or (text and updated)) and not bool(re.match(pattern, text)):
        print("Saisie incorrect, rentrez une adresse email valide")
        text = input(message)
    return text

def date_input(message, updated=False):
    text = input(message)
    pattern = r'^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'  # Format AAAA-MM-DD
    while (not updated or (text and updated)) and not bool(re.match(pattern, text)):
        print("Saisie incorrect, rentrez une date au format XXXX(année)-XX(mois)-XX(jour)")
        text = input(message)
    return text
