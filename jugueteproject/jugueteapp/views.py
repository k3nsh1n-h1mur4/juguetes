from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, UserManager
from jugueteproject.settings import BASE_DIR
from django.contrib.auth import authenticate
# Create your views here.

from jugueteapp.forms import UserForm, loginForm, workerForm

def index(request):
    return HttpResponse('Index')

def register(request):
    title = 'Registro de Usuario'
    form = UserForm(request.POST)
    #print(form.is_bound)
    #print(form)
    #print(form.data)
    #data = form.data
    #print(data)
    #print(form.is_valid())
    #for field in form:
    #    print(field.label_tag)
    #    print(field.name)
    print(form.default_renderer)
    for boundfield in form:
        print(boundfield)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        print(user)
        if user:
            print("Usuario creado")
        #ctx = form.get_context()
        #print(ctx.fields)
    return render(request, 'auth/register.html', {'form': form, 'title': title})
    
def login(request):
    title = 'LogIn'
    form = loginForm(request.POST)
    if request.method == 'POST':
        form = loginForm(request.POST)
        #print(form)
        email = form.data['email']
        password = form.data['password']
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
    return render(request, 'auth/login.html', {'form': form, 'title': title})
        
        
def registerW(request):
    title='Registro Trabajador'
    form = workerForm(request.POST)
    if request.method == 'POST':
        return render(request, 'worker/registerW.html', {'form': form})
    return render(request, 'worker/registerW.html', {'form': form, 'title': title})
    
