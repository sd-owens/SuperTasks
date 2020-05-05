from django.forms import PasswordInput, modelform_factory, ModelForm
from django.contrib.auth.models import User

from .models import Account

# Automatically creates a registration form from the User model
RegisterForm = modelform_factory(
    User,
    fields=("username", "password", "email"),
    widgets={"password": PasswordInput()}
)

"""
Form for user to update account settings
"""
class AccountSettingsForm(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = [
            "username",
            "user",
            "date_created",
        ]