import pytest
from input_validation import is_valid_email, is_valid_passwort

@pytest.mark.parametrize("email_valid", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
,   ("email@example.com")
,   ("firstname.lastname@example.com")
,   ("email@subdomain.example.com")
,   ("firstname+lastname@example.com")
,   ("email@example.com") 
,   ("1234567890@example.com") 
,   ("email@example-one.com")
,   ("_______@example.com")
,   ("email@example.name")
,   ("email@example.museum")
,   ("email@example.co.jp")
,   ("firstname-lastname@example.com")
])
def test_is_valid_email__gueltige_Adressen(email_valid):
    # arrange
    email_adress_to_be_tested = email_valid
    
    # act
    response = is_valid_email(email_valid)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email_invalid", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen,
,   ("plainaddress") 
,   ("#@%^%#$@#$@#.com"),
    ("@example.com"), 
    ("Joe Smith <email@example.com>"), 
    ("email.example.com"), 
    ("email@example@example.com"), 
    (".email@example.com"), 
    ("email.@example.com"), 
    ("email..email@example.com"), 
    ("email@example.com (Joe Smith)"), 
    ("email@example"), 
    ("email@-example.com"), 
    ("email@111.222.333.44444"), 
    ("email@example..com"), 
    ("Abc..123@example.com"),
])
def test_is_valid_email__ungueltige_Adressen(email_invalid):
    # arrange
    email_adress_to_be_tested = email_invalid
    
    # act
    response = is_valid_email(email_adress_to_be_tested)
    
    # assert
    assert response is False

@pytest.mark.parametrize("passwort_valid", [
    ('123Abc!?'),
    ('1ajdoaA!?'),
    ('123A*#+b?'),
    ('äüö%=)1dA'),
])
def test_is_valid_passwort__korrekt(passwort_valid):
    # arrange
    passwort_to_test = passwort_valid

    # act
    response = is_valid_passwort(passwort_to_test)

    # assert
    assert response is True

@pytest.mark.parametrize("passwort_invalid", [
    ('123AB!o'),
    ('aieg51h=!ad'),
    ('191OAKDW!='),
    ('äüö%=)adA'),
    ('Passwort123'),
])
def test_is_valid_passwort__inkorrekt(passwort_invalid):
    # arrange
    passwort_to_test = passwort_invalid

    # act
    response = is_valid_passwort(passwort_to_test)

    # assert
    assert response is False