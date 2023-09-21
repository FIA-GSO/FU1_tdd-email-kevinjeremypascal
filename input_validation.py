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
        print(validate_email(email, check_deliverability=False), 'ääää')
        return validate_email(email, check_deliverability=False) is not None
    except:
        return False