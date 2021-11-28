from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet
import app
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Afiliacion, Implicado, Partido, Individuo, Proceso

# Create your views here.
def index(request):
    return HttpResponse('HOLA')

#--------------------------------------------------------------------#
# 1 y 2 requerimiento
#--------------------------------------------------------------------#
def inicio_sesion_view(request):
    return render(request, 'app/InicioSesionV.html')

def iniciar_sesion_post(request):
    u = request.POST['username']
    p = request.POST['password']
    usuario = authenticate(username = u, password = p)

    if usuario is None:
        return render(request, 'app/ErrorInicioV.html')
    else:
        login(request, usuario)
        if request.user.is_active == False:
            return render(request, 'app/ErrorInicioV.html')
            
        if request.user.is_superuser == True:
            return redirect('app:pagina_administrador_view')
        else:
            return redirect('app:pagina_ciudadano_view')

def cerrar_sesion(request):
    logout(request)
    return render(request, 'app/InicioSesionV.html')
#--------------------------------------------------------------------#
# 3 requerimiento
#--------------------------------------------------------------------#
def registrarse_view(request):
    return render(request, 'app/RegistrarseV.html')

def registrarse_post(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    usuario = User()
    usuario.first_name = nombres
    usuario.last_name = apellidos
    usuario.username = username
    usuario.set_password(password)
    usuario.email= email

    try:
        usuario.save()
        return render(request, 'app/InicioSesionV.html')
    except:
        return render(request, 'app/ErrorRegistroV.html')
#--------------------------------------------------------------------#
# Home del ciudadano y del administrador
#--------------------------------------------------------------------#
def pagina_ciudadano_view(request):
    return render(request, 'app/PaginaCiuV.html')

def pagina_administrador_view(request):
    return render(request, 'app/PaginaAdminV.html')
#--------------------------------------------------------------------#
# 4 requerimiento. Cambiar datos de la cuenta
# Hay que corregir
#--------------------------------------------------------------------#
def CambiarDatosCuentaP_view(request):
    return render(request, 'app/CambiarDatosCuentaP.html')

def CambiarDatosCuentaPOSTP(request, id_user):
    actualizar_usu = User.objects.get(id = id_user) 

    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    actualizar_usu

    actualizar_usu.first_name = nombres
    actualizar_usu.last_name = apellidos
    actualizar_usu.username = username
    actualizar_usu.set_password(password)
    if actualizar_usu.email != email:
        actualizar_usu.email = email

    try:
        actualizar_usu.save()
        if actualizar_usu.is_superuser == True:
            return redirect('app:CambioExitosoP_view')
            # return render(request, 'app/InicioSesionV.html')
        else:
            return redirect('app:CambioExitosoP_view')
            # return render(request, 'app/InicioSesionV.html')
    except:
        if actualizar_usu.is_superuser == True:
            return render(request, 'app/ErrorCambioDatosP.html')
        else:
            return render(request, 'app/ErrorCambioDatosP.html')

def CambioExitosoP_view(request):
    return render(request, 'app/CambioExitosoP.html')

def ErrorCambioDatosP_view(request):
    return render(request, 'app/ErrorCambioDatosP.html')
#--------------------------------------------------------------------#
# 5 requerimiento. Crear partido político
#--------------------------------------------------------------------#
def CrearPartidoPoliticoP_view(request):  
    lista = User.objects.all()
    contexto = {
        'usuarios': lista
    }
    return render(request, 'app/CrearPartidoPoliticoP.html', contexto)

def CrearPartidoPoliticoPOSTP(request):
    if request.user.is_superuser == True:
        nombre = request.POST['nombre']
        usuario = request.user.id
        id_user = usuario
        user = User.objects.get(id = id_user) 
    
        p = Partido()
        p.nombre = nombre
        p.user = user
        p.save()

        # return redirect('app:ConsultarListaPartidosPoliticosCP_view')
        return redirect('app:pagina_administrador_view')
    else:
        return render(request, 'app/ErrorCuenta.html')    

def CrearPartidoPoliticoFormP_view(request):
    return render(request, 'app/CrearPartidoPoliticoP.html')
#--------------------------------------------------------------------#
# 6 requerimiento. Consultar la lista de partidos políticos
#--------------------------------------------------------------------#
def ConsultarListaPartidosPoliticosAP_view(request):
    def ordenar(e):
        return e[1]

    parti = Partido.objects.all()
    partidos = []
    for i in parti:
        afiliados = Afiliacion.objects.filter(partido = i)
        procesos = 0
        for j in afiliados:
            implicado = Implicado.objects.filter(afiliado = j)
            procesos += implicado.count()

        partidos.append((
            i, 
            procesos
        ))
    
    partidos.sort(key = ordenar)
    contexto = {
        'ConsultarListaPartidosPoliticosCP': partidos,
    }
    return render(request, 'app/ConsultarListaPartidosPoliticosAP.html', contexto)

def ConsultarListaPartidosPoliticosCP_view(request):
    parti = Partido.objects.all()
    partidos = []
    for i in parti:
        afiliados = Afiliacion.objects.filter(partido = i)
        procesos = 0
        for j in afiliados:
            implicado = Implicado.objects.filter(afiliado = j)
            procesos += implicado.count()

        partidos.append((
            i, 
            procesos
        ))

    contexto = {
        'ConsultarListaPartidosPoliticosCP': partidos,
    }
    
    return render(request, 'app/ConsultarListaPartidosPoliticosCP.html', contexto)
#--------------------------------------------------------------------#
# 7 requerimiento. Consultar un partido político
#--------------------------------------------------------------------#
def ConsultarPartidoPoliticoSAR_view(request):
    partidos = Partido.objects.all()
    contexto = {
        'partidos': partidos
    }
    return render(request, 'app/ConsultarPartidoPoliticoSAR.html', contexto)

def ConsultarPPSAR_post(request):
    pid = int(request.POST['partido'])
    partidos = Partido.objects.all()

    p = Partido.objects.get(id = pid)
    p.visitas += 1
    p.save()

    afiliados = Afiliacion.objects.filter(partido = p).order_by('individuo__apellidos')
    procesos = 0
    procesos_cul = 0
    for j in afiliados:
        if j.aprobado:
            implicado = Implicado.objects.filter(afiliado = j)
            procesos += implicado.count()
            for k in implicado:
                if k.culpable:
                    procesos_cul += 1
    
    context = {
        'partidos': partidos,
        'partido': p,
        'procesos': procesos,
        'procesos_cul': procesos_cul,
        'afiliados': afiliados
    }
    return render(request, 'app/ConsultarPartidoPoliticoSAR.html', context)
#--------------------------------------------------------------------#
# 8 requerimiento. Crear individuo
#--------------------------------------------------------------------#
def CrearIndividuoCSAR_view(request):
    return render(request, 'app/CrearIndividuoCSAR.html')

def CrearIndividuoASAR_view(request):
    return render(request, 'app/CrearIndividuoASAR.html')

def CrearIndividuoCSAR_post(request):
    id = request.user.id
    nombres = request.POST['nombre']
    apellidos = request.POST['apellidos']
    fechaN = request.POST['fechaN']

    i = Individuo()
    i.nombres = nombres
    i.apellidos = apellidos
    i.fecha_nacimiento = fechaN
    i.aprobado = False

    u = User()
    u = User.objects.get(id = id)
    i.user = u
    
    i.save()
    return redirect('app:CreacionPendiente_view')

def CrearIndividuoASAR_post(request):
    if request.user.is_superuser == True:
        id = request.user.id

        nombres = request.POST['nombre']
        apellidos = request.POST['apellidos']
        fechaN = request.POST['fechaN']
        
        i = Individuo()
        i.nombres = nombres
        i.apellidos = apellidos
        i.fecha_nacimiento = fechaN
        i.aprobado = True

        u = User.objects.get(id = id)
        i.user = u
    
        i.save()
        return redirect('app:CreacionExitosa_view')

def CreacionExitosa_view(request):
    return render(request,'app/CreacionIndividuoExitosa.html')

def CreacionPendinte_view(request):
    return render(request,'app/CreacionIndividuoPendiente.html')
#--------------------------------------------------------------------#
# 9 requerimiento. Aprobar individuo
#--------------------------------------------------------------------#
def AprobarIndividuoSAR_view(request):
    lista_individuo = Individuo.objects.all()  
    contexto = {
        'individuo': lista_individuo
    }
    return render(request, 'app/AprobarIndividuoSAR.html', contexto)

def AprobarIndividuoSAR_post(request):
    id = int(request.POST['individuo']) 
    i = Individuo.objects.get(id = id)
    i.aprobado = True
    i.save()
    return redirect('app:AprobarExitoso_view')

def AprobarExitoso_view(request):
    return render(request, 'app/AprobarExitoso.html')
#--------------------------------------------------------------------#
# 10 requerimiento. Consultar lista de individuos
#--------------------------------------------------------------------#
def ConsultarListaIndiCP_view(request):
    def ordenar(e):
        return e[2]
    
    indi = Individuo.objects.all()
    individuos = []
    for i in indi:
        afiliados = Afiliacion.objects.filter(individuo = i)
        procesos = 0
        for j in afiliados:
            implicado = Implicado.objects.filter(afiliado = j)
            procesos += implicado.count()

        individuos.append((
            i, 
            afiliados.last(),
            procesos
        ))

    individuos.sort(key = ordenar)
    contexto = {
        'individuos': individuos,
    }
    return render(request, 'app/ConsultarListaIndiCP.html', contexto)

def ConsultarListaIndiAP_view(request):
    def ordenar(e):
        return e[2]
    
    indi = Individuo.objects.all()
    individuos = []
    for i in indi:
        afiliados = Afiliacion.objects.filter(individuo = i)
        procesos = 0
        for j in afiliados:
            implicado = Implicado.objects.filter(afiliado = j)
            procesos += implicado.count()

        individuos.append((
            i, 
            afiliados.last(),
            procesos
        ))

    individuos.sort(key = ordenar)

    contexto = {
        'individuos': individuos,
    }
    return render(request, 'app/ConsultarListaIndiAP.html', contexto)
#--------------------------------------------------------------------#
# 11 requerimiento. Consultar individuo
#--------------------------------------------------------------------#
def ConsultarIndividuo_view(request):
    individuos = Individuo.objects.all()
    context = {
        'individuos': individuos
    }
    return render(request, 'app/ConsultarIndividuo.html', context)

def ConsultarIndividuo_post(request):
    def ordenar(e):
        return e.proceso.fecha_inicio
    id_indi = int(request.POST['individuo'])
    individuos = Individuo.objects.all()
    i = Individuo.objects.get(id = id_indi)
    i.visitas += 1
    i.save()

    afiliaciones = Afiliacion.objects.filter(individuo = i).order_by('fecha_ingreso')
    impli = []
    implicados = []

    for a in afiliaciones:
        impli.append(Implicado.objects.filter(afiliado = a))

    for a in impli:
        for j in a:
            implicados.append(j)

    # implicados.order_by('proceso__fecha_inicio')
    implicados.sort(key = ordenar)


    context = {
        'i': i,
        'individuos': individuos,
        'afiliaciones': afiliaciones,
        'implicados': implicados
    }

    return render(request, 'app/ConsultarIndividuo.html', context)
#--------------------------------------------------------------------#
# 12 requerimiento. Afiliar individuo a partido
#--------------------------------------------------------------------#
def AfiliarIndividuoASAR_view(request):
    if request.user.is_superuser:
        individuos = Individuo.objects.all()
        partidos = Partido.objects.all()

        context = {
            'individuos': individuos,
            'partidos': partidos
        }
        return render(request, 'app/AfiliarIndividuoASAR.html', context)

def AfiliarIndividuoCSAR_view(request):
    individuos = Individuo.objects.all()
    partidos = Partido.objects.all()

    context = {
        'individuos': individuos,
        'partidos': partidos
    }
    return render(request, 'app/AfiliarIndividuoCSAR.html', context)

def AfiliarIndividuoASAR_post(request):
    if request.user.is_superuser:
        indi_id = int(request.POST['individuo_id'])
        parti_id = int(request.POST['partido_id'])
        fechai = request.POST['fecha-ingreso']
        fechas = request.POST['fecha-salida']

        i = Individuo.objects.get(id = indi_id)
        p = Partido.objects.get(id = parti_id)

        afiliar = Afiliacion()
        afiliar.individuo = i
        afiliar.partido = p
        afiliar.fecha_ingreso = fechai;
        afiliar.fecha_salida = fechas;
        afiliar.aprobado = True
        afiliar.save()

        return render(request, 'app/HabExitoso.html') 

def AfiliarIndividuoCSAR_post(request):
    indi_id = int(request.POST['individuo_id'])
    parti_id = int(request.POST['partido_id'])
    fechai = request.POST['fecha-ingreso']
    fechas = request.POST['fecha-salida']

    i = Individuo.objects.get(id = indi_id)
    p = Partido.objects.get(id = parti_id)

    afiliar = Afiliacion()
    afiliar.individuo = i
    afiliar.partido = p
    afiliar.fecha_ingreso = fechai;
    afiliar.fecha_salida = fechas;
    afiliar.aprobado = False
    afiliar.save()

    return redirect('app:CreacionPendiente_view')  
#--------------------------------------------------------------------#
# 13 requerimiento. Aprobar afiliación - ADMON
#--------------------------------------------------------------------#
def AprobarAfiliacionSAR_view(request):
    if request.user.is_superuser:
        afiliaciones = Afiliacion.objects.all()
        context = {
            'afiliaciones': afiliaciones
        }
        return render(request, 'app/AprobarAfiliacionSAR.html', context)

def AprobarAfiliacionSAR_post(request):
    if request.user.is_superuser:
        afi_id = int(request.POST['afiliacion'])
        a = Afiliacion.objects.get(id = afi_id)
        a.aprobado = True
        a.save()
        return redirect('app:AprobarExitoso_view')
#--------------------------------------------------------------------#
# 14 requerimiento. Crear un proceso
#--------------------------------------------------------------------#
def CrearProcesoASAR_view(request):
    if request.user.is_superuser:
        return render(request, 'app/CrearProcesoASAR.html')

def CrearProcesoCSAR_view(request):
    return render(request, 'app/CrearProcesoCSAR.html')

def CrearProcesoASAR_post(request):
    if request.user.is_superuser:
        proceso = Proceso()
        id_cre = request.user.id

        titulo = request.POST['titulo']
        fechaI = request.POST['fecha-i']
        fechaF = request.POST['fecha-f']
        abiocer = request.POST['ab-ce']
        entidad = request.POST['entidad']
        monto = request.POST['monto']
        comentarios = request.POST['comentarios']

        proceso.titulo = titulo
        proceso.fecha_inicio = fechaI
        proceso.fecha_fin = fechaF
        proceso.abierto = True if abiocer == '1' else False
        proceso.entidad = entidad
        proceso.monto = monto
        proceso.comentarios = comentarios
        proceso.aprobado = True
        proceso.user = User.objects.get(id = id_cre)

        proceso.save()

        return render(request, 'app/HabExitoso.html') 

def CrearProcesoCSAR_post(request):
    proceso = Proceso()
    id_cre = request.user.id

    titulo = request.POST['titulo']
    fechaI = request.POST['fecha-i']
    fechaF = request.POST['fecha-f']
    abiocer = request.POST['ab-ce']
    entidad = request.POST['entidad']
    monto = request.POST['monto']
    comentarios = request.POST['comentarios']

    proceso.titulo = titulo
    proceso.fecha_inicio = fechaI
    proceso.fecha_fin = fechaF
    proceso.abierto = True if abiocer == '1' else False
    proceso.entidad = entidad
    proceso.monto = monto
    proceso.comentarios = comentarios
    proceso.aprobado = False
    proceso.user = User.objects.get(id = id_cre)

    proceso.save()

    return redirect('app:CreacionPendiente_view')  
#--------------------------------------------------------------------#
# 15 requerimiento. Aprobar un proceso
#--------------------------------------------------------------------#
def AprobarProcesoASAR_view(request):
    if request.user.is_superuser:
        procesos = Proceso.objects.all()
        context = {
            'procesos': procesos
        }
        return render(request, 'app/AprobarProcesoSAR.html', context)

def AprobarProcesoASAR_post(request):
    if request.user.is_superuser:
        id_pro = int(request.POST['procesos'])
        proceso: Proceso = Proceso.objects.get(id = id_pro)
        proceso.aprobado = True
        proceso.save()
        return redirect('app:AprobarExitoso_view')
#--------------------------------------------------------------------#
# 16 requerimiento. Implicar Afiliado
#--------------------------------------------------------------------#
def ImplicarAfiliadoASAR_view(request):
    afiliados = Afiliacion.objects.all()
    procesos = Proceso.objects.all()

    context = {
        'afiliados': afiliados,
        'procesos': procesos
    }
    return render(request, 'app/ImplicarAfiliadoASAR.html', context)

def ImplicarAfiliadoCSAR_view(request):
    afiliados = Afiliacion.objects.all()
    procesos = Proceso.objects.all()

    context = {
        'afiliados': afiliados,
        'procesos': procesos
    }
    return render(request, 'app/ImplicarAfiliadoCSAR.html', context)

def ImplicarAfiliadoASAR_post(request):
    if request.user.is_superuser:
        id_afi = int(request.POST['afiliado'])
        id_pro = int(request.POST['proceso'])
        fechaIm = request.POST['fecha-i']
        acusacion = request.POST['acusacion']
        culpable = False if request.POST['cu-in'] == '0' else True
        pena = request.POST['pena']
        comentarios = request.POST['comentarios']

        implicar = Implicado()
        implicar.fecha = fechaIm
        implicar.acusacion = acusacion
        implicar.culpable = culpable
        implicar.pena = pena
        implicar.comentarios = comentarios

        implicar.afiliado = Afiliacion.objects.get(id = id_afi)
        implicar.proceso = Proceso.objects.get(id = id_pro)

        implicar.save()
        
        return redirect('app:AprobarExitoso_view')

def ImplicarAfiliadoCSAR_post(request):
    id_afi = int(request.POST['afiliado'])
    id_pro = int(request.POST['proceso'])
    fechaIm = request.POST['fecha-i']
    acusacion = request.POST['acusacion']
    culpable = False if request.POST['cu-in'] == '0' else True
    pena = request.POST['pena']
    comentarios = request.POST['comentarios']

    implicar = Implicado()
    implicar.fecha = fechaIm
    implicar.acusacion = acusacion
    implicar.culpable = culpable
    implicar.pena = pena
    implicar.comentarios = comentarios

    implicar.afiliado = Afiliacion.objects.get(id = id_afi)
    implicar.proceso = Proceso.objects.get(id = id_pro)

    implicar.save()
    
    return redirect('app:pagina_ciudadano_view')
#--------------------------------------------------------------------#
# 17 requerimiento. Mostrar un proceso
#--------------------------------------------------------------------#
def ConsultarProceso_view(request):
    procesos = Proceso.objects.all()
    context = {
        'procesos': procesos
    }
    return render(request, 'app/ConsultarProceso.html', context)

def ConsultarProceso_post(request):
    id_pro = int(request.POST['proceso'])
    procesos = Proceso.objects.all()
    p = Proceso.objects.get(id = id_pro)
    p.visitas += 1
    p.save()
    implicados = Implicado.objects.filter(proceso = p)

    context = {
        'proceso': p,
        'procesos': procesos,
        'implicados': implicados
    }

    return render(request, 'app/ConsultarProceso.html', context)
#--------------------------------------------------------------------#
# 18 requerimiento. Habilitar/deshabilitar ciudadano - ADMON
#--------------------------------------------------------------------#
def HabDesSAR_view(request):
    lista_usuarios = User.objects.all()  
    contexto = {
        'User': lista_usuarios
    }
    return render(request, 'app/HabilitarDeshabilitarSAR.html', contexto)

def HabDesSAR_post(request):
    if request.user.is_superuser == True:
        print(request.POST['individuo'], request.POST['opcion'])
        id = int(request.POST['individuo'])
        accion = request.POST['opcion']
        u = User.objects.get(id = id)
        if accion == 'habilitar':
            u.is_active = True
        else:
            u.is_active = False
    
        u.save()
        return render(request, 'app/HabExitoso.html')
    else:
        return render(request, 'app/ErrorCambioDatosP.html')
    
def HabDesEXI_view(request):
    return render(request, 'app/HabExitoso.html')  
#--------------------------------------------------------------------#



def usuarios_view(request):
    lista = User.objects.all()
    contexto = {
        'usuarios':lista
    }
    return render(request, 'app/usuarios.html',contexto)

def ErrorCuenta_view(request):
    return render(request, 'app/ErrorCuenta.html') 

def acerca_view(request):
    return render(request, 'app/acerca.html')



