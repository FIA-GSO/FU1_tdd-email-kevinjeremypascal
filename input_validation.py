import re   #regular Expressions
from email_validator import validate_email
def is_valid_email(email:str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid
    False -- email is not valid
    """
    try:
        print(validate_email(email, check_deliverability=False, test_environment=True), 'ääää')
        return validate_email(email, check_deliverability=False) is not None
    except:
        return False
    
def is_valid_passwort(passwort:str) -> bool:
    checkNumber = re.compile(r"\d")
    checkLowerCase = re.compile(r"[a-z]")
    checkUpperCase = re.compile(r"[A-Z]")
    checkSpecialChar = re.compile(r'''[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]''')
    pwLen = len(passwort)

    containsNumber = bool(checkNumber.search(passwort))
    containsLowerCase = bool(checkLowerCase.search(passwort))
    containsUpperCase = bool(checkUpperCase.search(passwort))
    containsSpecialChar = bool(checkSpecialChar.search(passwort))

    if pwLen < 12 and pwLen >= 8:
        if all((containsNumber, containsLowerCase, containsUpperCase, containsSpecialChar)):
            return True

    if pwLen > 19:
        if sum((containsNumber, containsLowerCase, containsUpperCase, containsSpecialChar)) >= 2:
            return True

    return False