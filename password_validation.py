import re

def password_validator(password)-> [bool,str]:
    pass_pattern = r'^(?=.*[A-Za-z0-9])[A-Za-z0-9 ?!%+$]+$'
    if len(password) < 8: 
        return False,"Password is too short"
    #if password first char is  ?!%+$ is False
    if password[0] in "?!%+$":
        return False,"Password is not valid,no special charachter at the beginning"
    if not re.match(pass_pattern, password):
        return False,"Password is not valid, plese use only letters, numbers and the following special characters: ?!%+…"
    if not re.search("[a-z,A-Z]", password): 
        return False,"Password is not valid, please use at least one lowercase letter and one uppercase letter"
    return True,"Password is valid"