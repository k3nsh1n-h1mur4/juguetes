from django.shortcuts import render, HttpResponse, HttpResponse
from jugueteproject.settings import BASE_DIR
# Create your views here.

from jugueteapp.forms import UserForm

def index(request):
    return HttpResponse('Index')

def register(request):
    title = 'Registro de Usuario'
    form = UserForm(request.POST)
    print(form.is_bound)
    print(form)
    print(form.data)
    data = form.data
    print(data)
    print(form.is_valid())
    return render(request, 'auth/register.html', {'form': form, 'title': title})
    