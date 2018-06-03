from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from users.models import UserProfile


def validate_account(username, email, password, conf_password):
    try:
        validate_username(username)
        validate_email(email)
        validate_password(password, conf_password)
    except ValidationError as error:
        return list(error)[0]


def validate_username(username):
    if username_exists(username):
        raise ValidationError('Username already exists') 
    elif len(username) < 5:
        raise ValidationError('Username should have min.8 chars') 


def username_exists(username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return False
    return True


def validate_email(email):
    if '@' not in email:
        raise ValidationError('Unproper format of email')


def validate_password(password, conf_password):
    if len(password) < 5:
        raise ValidationError('Password should have min.8 chars')
    elif password != conf_password:
        raise ValidationError('Passwords doesn`t match')
