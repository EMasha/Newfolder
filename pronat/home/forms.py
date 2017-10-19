from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.admin import User
from django import forms
from .models import prona




User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if username and password:
                if not user:
                    raise forms.ValidationError("This user does not exist")
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is not longer active")
            return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    def clean(self, *args, **kwargs):
        print (self.cleaned_data)
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        print (email, email2)
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been register")

            return super(UserRegistrationForm, self).clean(*args, **kwargs)

