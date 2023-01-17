from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    email = forms.EmailField(label='Email', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=150)

