import re

def check_password(password) -> bool:
    """CHECKS IF THE PASSWORD IS VALID"""
    if len(password) < 8:
        return False
    elif password == "password" or password == "Password":
        return False
    elif re.search("[0-9]", password) is None:
        return False
    elif re.search("[a-zA-Z]", password) is None:
        return False
    
    return True

def check_email(email) -> bool:
    """CHECKS IF THE E-MAIL IS VALID"""
    if len(email) > 64:
        return False
    elif re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email) is None:
        return False
    
    return True

def check_username(name) -> bool:
    """CHECKS IF THE USERNAME IS VALID OR NOT"""
    if len(name) == 0:
        return False
    elif len(name) > 32:
        return False
    
    return True