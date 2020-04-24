from django.forms import PasswordInput, modelform_factory
from django.contrib.auth.models import User

# Automatically creates a registration form from the User model
RegisterForm = modelform_factory(
    User,
    fields=("username", "password", "email"),
    widgets={"password": PasswordInput()}
)
