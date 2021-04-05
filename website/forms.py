from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=25)
    last_name = forms.CharField(required=True, max_length=25)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit = False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['firs_tname']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user