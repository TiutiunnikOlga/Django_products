from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from loging.models import User


class LoginRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
