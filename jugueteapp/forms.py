from django import forms

from .models import User, workerModel

class UserForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    username = forms.CharField(label='Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control' }))
    password = forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     
    
class loginForm(forms.Form):
    username= forms.EmailField(label='Usuario', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class workerForm(forms.Form):
    TURNO = [
        ('MATUTINO', 'MATUTINO'),
        ('VESPERTINO', 'VESPERTINO'),
        ('NOCTURNO', 'NOCTURNO'),
        ('JORNADA ACUMULADA', 'JORNADA ACUMULADA'),
    ]

    T_CONTR = [
        ('02 BASE', '02 BASE'),
        ('03 TEMPORAL', '03 TEMPORAL'),
        ('08 EVENTUAL', '08 EVENTUAL'),
        ('CONFIANZA B', 'CONFIANZA B'),
    ]

    matricula = forms.CharField(label='Matrícula', max_length=100, widget=forms.TextInput({'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre Completo', max_length=250, widget=forms.TextInput({'class':'form-control'}))
    categoria = forms.CharField(label='Categoría', max_length=100, widget=forms.TextInput({'class': 'form-control'}))
    antiguedad = forms.CharField(label='Antiguedad', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adscripcion = forms.CharField(label='Unidad de Adscripción', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    t_contr = forms.ChoiceField(label='Tipo de Contratación', widget=forms.Select(attrs={'class': 'form-control'}), choices=T_CONTR,)
    turno = forms.ChoiceField(label='Turno', widget=forms.Select(attrs={'class': 'form-control'}), choices=TURNO,)
    email = forms.CharField(label='Email', max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    domicilio = forms.CharField(label='Domicilio Particular', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono =  forms.CharField(label='Teléfono', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
