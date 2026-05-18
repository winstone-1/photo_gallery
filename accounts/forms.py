from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    """Form for new user registration."""

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    """Form for editing user profile details."""

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }