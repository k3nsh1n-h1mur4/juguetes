from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, UserManager
from jugueteproject.settings import BASE_DIR
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from jugueteapp.forms import UserForm, loginForm, workerForm, childForm 
from jugueteapp.models import workerModel, childModel

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
    #print(request.user.is_authenticated)
    title = 'LogIn'
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        #print(form)
        m = User.objects.get(username=request.POST['username'])
        print("m")
        print(m)
        if m.check_password(request.POST['password']):
            request.session['user_id'] = m.id
            return redirect('registerW')
            #return HttpResponse("Estas Logueado")
        else:
            return HttpResponse("no logueado")
        #email = form.data['email']
        #password = form.data['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(authenticate(request, username=username, password=password))
            login(request)
            #print(request.user)

            #print(user)
            #if user is not None:
            #    login(request, user)
            #    print("Usuario autenticado")
    return render(request, 'auth/login.html', {'form': form, 'title': title})




@login_required       
def registerW(request):
    print(request.user.id)
    print(request.user)

    title='Registro Trabajador'
    form = workerForm()
    if request.method == 'POST':
        form = workerForm(request.POST or None)
        #print(form)
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
            worker = workerModel.objects.create(matricula=matricula, nombre=nombre, categoria=categoria, antiguedad=antiguedad, adscripcion=adscripcion, t_contr=t_contr, turno=turno, email=email, domicilio=domicilio, telefono=telefono, user_id=request.user.id)
            print(worker)
            if worker is not None:
                print("Trabajador Registrado")
                return redirect('list')
            else:
                print("No registrado")
    return render(request, 'worker/registerW.html', {'form': form, 'title': title})


@login_required
def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        return HttpResponse("Deslogueado")

@login_required
def list(request):
    title = 'Listado General Trabajadores'
    if request.method == 'GET':
        ctx = workerModel.objects.all()
        if ctx is None:
            print('No hay elementos que mostrar')
    return render(request, 'worker/list.html', {'ctx': ctx, 'title': title}) 

@login_required
def registerC(request, id):
    form = childForm()
    title = 'Registro Hijos(as)'
    try:
        pk = workerModel.objects.get(pk=id)
        print(pk)
        #form = childForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            f_nac = form.cleaned_data['f_nac']
            edad = form.cleaned_data['edad']
            sexo = form.cleaned_data['sexo']
            entregado = form.cleaned_data['entregado']
            child = childModel.objects.create(nombre=nombre.upper(), f_nac=f_nac, edad=edad, sexo=sexo.upper(), entregado=entregado.upper(), worker_id=pk)
            if child is not None:
                print('Registro Realizado')
            else:
                return HttpResponse('No realizado')
        return render(request, 'childs/registerC.html', {'form': form, 'title': title, 'pk': pk})
    except workerModel.DoesNotExist:
        raise Http404('Worker does not exist')

    return render(request, 'childs/registerC.html', {'form': form, 'title': title, 'id':id})

@login_required
def logout_views(request):
    logout(request)
    return redirect('login_user')