import os
from django.http import Http404, FileResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, UserManager
from jugueteproject.settings import BASE_DIR
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from fpdf import FPDF
import sqlite3
import qrcode
from qrcode import QRCode
from PIL import Image
import pyqrcode
import io
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle


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
def deleteW(request, id):
    try:
        id = workerModel.objects.get(id=id).delete()
        print(id)
        message = 'Registro Eliminado'
        return redirect('list', {'message': message})
    except:
        return HttpResponse('Registro no Eliminado')

@login_required
def registerC(request, id):
    form = childForm()
    #print(form)
    title = 'Registro Hijos(as)'
    if request.method == 'POST':
        form = childForm(request.POST or None)
    #formato = '%Y/%m/%d'
    #fecha1 = datetime.now()
        try:
            pk = workerModel.objects.get(pk=id)
            print(pk)
        #form = childForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                f_nac = form.cleaned_data['f_nac']
                #fecha2 = datetime.strptime(f_nac, formato)
                #days = fecha1 - fecha2
                #age = days.days / 365.2425
                edad = form.cleaned_data['edad']
                print(edad)
                sexo = form.cleaned_data['sexo']
                entregado = form.cleaned_data['entregado']
                child = childModel.objects.create(nombre=nombre.upper(), f_nac=f_nac, edad=edad, sexo=sexo.upper(), entregado=entregado.upper(), worker_id=pk)
                print(child)
                if child is not None:
                    print('Registro Realizado')
                    return redirect('listC')
                else:
                    return HttpResponse('No realizado')
            return render(request, 'childs/registerC.html', {'form': form, 'title': title, 'pk': pk})
        except workerModel.DoesNotExist:
            raise Http404('Worker does not exist')

    return render(request, 'childs/registerC.html', {'form': form, 'title': title, 'id':id})


@login_required
def listC(request):
    error = 'No hay Elementos que mostrar'
    title = 'Listado Hijos(as)'
    if request.method == 'GET':
        ctx = childModel.objects.all().order_by('id')
        if ctx is None:
            error = 'No hay Elementos que mostrar'
    return render(request, 'childs/list.html', {'ctx': ctx, 'title': title, 'error': error})


@login_required
def deleteC(request, id): 
    id = childModel.objects.get(id=id).delete()
    print(id)
    return redirect('list')
    


def createImage(data):
    #qr = pyqrcode.create(data)
    #img = qr.png('image.png', scale=5, encode='binary')
    qr = QRCode()
    qr.add_data(data)
    img = qr.make_image()
    #img.show()
    #img.show()
    #print(img)
    return img


def createQR(request, id):
    id = id
    con = sqlite3.connect('db.sqlite3')
    print(con)
    cur = con.cursor() 
    rows = cur.execute("SELECT * FROM worker INNER JOIN chailds WHERE worker.id=chailds.worker_id_id AND chailds.worker_id_id={0}".format(id))
    result = rows.fetchall()
    print(len(result))
    con.commit()
    qr = QRCode()
    qr.add_data(result)
    img = qr.make_image()
    return render(request, 'worker/qrcode.html', {'img': img})
    



@login_required
def valePdf(request, id):
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    r = request 
    print(r)
    id = id
    global FPDF
    con = sqlite3.connect('db.sqlite3')
    print(con)
    cur = con.cursor() 
    rows = cur.execute("SELECT * FROM worker INNER JOIN chailds WHERE worker.id=chailds.worker_id_id AND chailds.worker_id_id={0}".format(id))
    result = rows.fetchall()
    print(len(result))
    con.commit()
    createImage(result)
    #qr = QRCode()
    #qr.add_data(result)
    #img = qr.make_image()
    #img.save('qrcode' + ' ' + result[0][2] + '.png')
    #print(img)
    #cur.close()
    #db.close()
    class FPDF(FPDF):
        from fpdf import FPDF
        def setHeader(self):
            directory_path = os.path.join(BASE_DIR, 'static')
            img = os.path.join(directory_path, 'sntss-logo.png')
            self.image(img, x=3.5, y=3.5, h=30, w=30)
            img1 = os.path.join(directory_path, 'fuertes.png')
            self.image(img1, x=175, y=3.5, w=30, h=30)
            self.set_font('helvetica', size=12, style='B')
            self.set_xy(x=30, y=7)
            self.multi_cell(w=150, h=5, txt='SINDICATO NACIONAL DE TRABAJADORES DEL SEGURO SOCIAL\n SECCIÓN III, JALISCO\n SECRETERÍA DE ACTOS Y FESTEJOS\n REGISTRO JUGUETES 2023', align='C')
        def setDataGrls(self):
            self.set_font('helvetica', size=10, style='B')
            self.text(x=10, y=38, txt='DATOS GENERALES TRABAJADOR:')
        def setDataWorker(self):
            self.set_font('helvetica', size=8, style='B')
            self.set_xy(x=10, y=45)
            self.cell(txt='Nombre:')
            self.set_xy(x=25, y= 44.5)
            self.cell(txt=result[0][2], border=0, fill=False)
            self.set_xy(x=90, y=45)
            self.cell(txt='Matrícula: ', border=0, fill=False)
            self.set_xy(x=110, y=44.5)
            self.set_fill_color(230, 230, 0)
            self.cell(txt=result[0][1], border=0, fill=True)
            self.set_xy(x=130 , y=45)
            self.cell(txt='Adscripción:', border=0, fill=0)
            self.set_xy(x=150, y=43.5)
            self.set_font('helvetica', size=8, style='B')
            self.multi_cell(w=55, h=5, txt=result[0][5], align='J', border=0, fill=False)
        def setChildrens(self):
            self.set_font('helvetica', size=10, style='B')
            self.text(x=10, y=60, txt='DATOS NIÑOS(AS) REGISTRADOS: ')
            self.set_xy(x=10, y=65)
            self.set_font('helvetica', size=8, style='B')
            self.cell(txt='Nombre niño(a):', border=0, fill=0)
            self.set_xy(x=35, y=64.5)
            self.cell(txt=result[0][14], border=0, fill=0)
            self.set_xy(x=90, y=64.5)
            self.cell(txt='Edad:')
            edad = str(result[0][16])
            self.cell(txt=edad)
            self.set_xy(x=130, y=65)
            self.cell(txt='Sexo:')
            self.set_xy(x=140 , y=64.5)
            self.cell(txt=result[0][17], border=0, fill=0)
            path = os.path.join(BASE_DIR, 'pdfs')
            

            #print(dir(im))
            #self.image(o, x=40, y=70)



    pdf = FPDF()
    pdf.add_page()
    pdf.setHeader()
    pdf.setDataGrls()
    pdf.setDataWorker()
    pdf.setChildrens()
    pdf.output("f.pdf")
    
    return HttpResponse(result)
    #return render(request, 'worker/qrcode.html', {'result': result})
    #res = HttpResponse(render(request, 'worker/qrcode.html', {'img': img}))
    #return res
    #res.headers['Content-Type'] = 'application/pdf'
    #res.headers['Content-Disposition'] = 'attachment; filename=asdasd.pdf'
    #return HttpResponse(result)
    #return res


@login_required
def getQrcode(request, id):
    id = id
    db = sqlite3.connect('db.sqlite3')
    print(db)
    cur = db.cursor() 
    rows = cur.execute("SELECT * FROM worker INNER JOIN chailds WHERE worker.id=chailds.worker_id_id AND chailds.worker_id_id={0}".format(id))
    result = rows.fetchall()
    print(len(result))
    db.commit()
    cur.close()
    db.close()
    return render(request, 'worker/qrcode.html', {'result': result})


@login_required
def logout_views(request):
    logout(request)
    return redirect('login_user')



def createpdf(request, id):
    id = id
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    result = cur.execute("SELECT * FROM worker INNER JOIN chailds WHERE worker.id=chailds.worker_id_id AND chailds.worker_id_id={0}".format(id))
    rows = result.fetchall()
    result = con.commit()
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    directory_path = os.path.join(BASE_DIR, 'static')
    img = os.path.join(directory_path, 'sntss-logo.png')
    img1 = os.path.join(directory_path, 'fuertes.png')

    p.drawImage(img, 5, 750, 80, 80)
    p.drawImage(img1, 500, 750, 80, 80)
    
    p.drawString(90, 770, 'SINDICATO NACIONAL DE TRABAJADORES DEL SEGURO SOCIAL')
    p.drawString(90, 740, 'SECCIÓN III, JALISCO')

    p.drawString(10, 10, rows[0][2])
    p.showPage()
    p.save()
    buffer.seek(0)
    cur.close()
    con.close()
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
