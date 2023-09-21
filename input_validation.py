import re   #regular Expressions
from email_validator import validate_email
def is_valid_email(email:str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid
    False -- email is not valid
    """

    return validate_email(email) is not None