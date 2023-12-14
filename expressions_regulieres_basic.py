import re
def recherche(mot, chaine):
    pattern = re.escape(mot)
    match = re.search(pattern, chaine)
    if match :
        return True
    else :
        return False
    
def verifie_chaine(chaine):
    match = re.search(r"\d" , chaine)
    if match :
        return True
    else :
        return False
    
def remplace(chaine):
    match = re.sub(r"\s" , "-" , chaine )
    return match 

def verifie_numero(numero):
    match = re.search(r"^\d{2}-\d{3}-\d{4}$" , numero)
    if match :
        return True
    else :
        return False

def verifie_email(email):
    match = re.search(r"^\w+@\w+\.(com|ma|org|info|ru)$" , email)
    if match :
        return True
    else :
        return False