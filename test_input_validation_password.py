import pytest
from password_validation import password_validator

@pytest.mark.parametrize("password_valid", [
    ("test12345"),
#    ("test1234!"),
#    ("test1234!$"),
#    ("test1234!$%"),
#    ("test1234!$%&"),
#    ("test1234!$%&/"),
#    ("test1234!$%&/()")
]
)

def test_password_validator(password_valid):
    response = password_validator(password_valid)
    assert response[0] is True,"Password is valid"

@pytest.mark.parametrize("password_too_short", [
    ("short"),
]
)

def test_password_validator_not_valid(password_too_short):
    response = password_validator(password_too_short)
    assert response[0] is False,"Password is too short"

def test_password_validator_not_valid_chars():
    password = "notvalid#char"
    response = password_validator(password)
    assert response[0] is False,"Password is not valid, plese use only letters, numbers and the following special characters: ?!%+$"

def test_password_validator_not_one_uppercase():
    password = "test1234!$%&/()"
    response = password_validator(password)
    assert response[0] is False,"Password is not valid, please use at least one lowercase letter and one uppercase letter"

def test_password_validator_not_one_lowercase():
    password = "TESST1234!$%&/()"
    response = password_validator(password)
    assert response[0] is False,"Password is not valid, please use at least one lowercase letter and one uppercase letter"

def test_password_validator_no_special_char_at_beginning():
    password = "!test1234"
    response = password_validator(password)
    assert response[0] is False,"Password is not valid,no special charachter at the beginning"