from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, UserManager
from jugueteproject.settings import BASE_DIR
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from jugueteapp.forms import UserForm, loginForm, workerForm
from .models import workerModel

@login_required
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
            login(request, user)
            print(user.id)
            print("Usuario creado")
            return redirect('registerW')
        #ctx = form.get_context()
        #print(ctx.fields)
    return render(request, 'auth/register.html', {'form': form, 'title': title})


@login_required
def login_user(request):
    print(request.user.is_authenticated)
    title = 'LogIn'
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        #print(form)
        #email = form.data['email']
        #password = form.data['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate(request, username=username, password=password)
            login(request)
            print(request.user)

            #print(user)
            #if user is not None:
            #    login(request, user)
            #    print("Usuario autenticado")
    return render(request, 'auth/login.html', {'form': form, 'title': title})




@login_required       
def registerW(request):
    print(request.user.id)
    title='Registro Trabajador'
    form = workerForm(request.POST or None)
    if request.method == 'POST':
        form = workerForm(request.POST or None)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            nombre = form.cleaned_data['nombre']
            categoria = form.cleaned_data['categoria']
            antiguedad = form.cleaned_data['antiguedad']
            adscripcion = form.cleaned_data['adscripcion']
            t_contr = form.cleaned_data['t_contr']
            turno = form.cleaned_data['turno']
            email = form.cleaned_data['email']
            domicilio = form.cleaned_data['domicilio']
            telefono = form.cleaned_data['telefono']
            worker = workerModel.objects.add(matricula=matricula, nombre=nombre, categoria=categoria, antiguedad=antiguedad, adscripcion=adscripcion, t_contr=t_contr, turno=turno, email=email, domicilio=domicilio, telefono=telefono, user_id=request.user.id)
            if worker is not None:
                print("Trabajador Registrado")
                return redirect('list')
    return render(request, 'worker/registerW.html', {'form': form, 'title': title})


@login_required
def list(request):
    title = 'Listado General Trabajadores'
    if request.method == 'GET':
        ctx = workerModel.objects.all()
        if ctx is None:
            print('No hay elementos que mostrar')
    return render(request, 'worker/list.html', {'ctx': ctx, 'title': title}) 

@login_required
def logout_views(request):
    logout(request)
    return redirect('login_user')