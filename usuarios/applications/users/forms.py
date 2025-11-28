from django import forms 
#
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegisterForm

    class Meta:
        """Meta definition for UserForm."""

        model = User
        fields = ('__all__')
