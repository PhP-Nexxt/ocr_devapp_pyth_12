import re # Regex > Permet de gerer les validateurs



def str_input(message, updated=False):
    text = input(message)
    pattern = r'^.{3,}$'  # Au moins 3 caractères
    while (not updated and not bool(re.match(pattern, text))) or (text and updated and not bool(re.match(pattern, text))):
        print("Saisie incorrect, le texte doit contenir au moins 3 caracteres")
        text = input(message)
    return text

def int_input(message, updated=False):
    text = input(message)
    pattern = r'^\d+$'  # Entier positif uniquement
    while (not updated and not bool(re.match(pattern, str(text)))) or (text and updated and not bool(re.match(pattern, str(text)))):
        print("Saisie incorrect, il faut entrer un nombre entier positif")
        text = input(message)
    return int(text)

