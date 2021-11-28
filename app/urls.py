from django.urls import path
from django.urls.resolvers import URLPattern
from .import views


app_name = 'app'
urlpatterns = [
    # url(r'hitcount/',include('hitcount.urls', namespace='hitcount')),
    path('', views.index, name='index'),
    # Requerimiento 1, 2, 3
    path('inicio/', views.inicio_sesion_view, name="inicio_sesion_view"),
    path('post_inicio/', views.iniciar_sesion_post, name ='iniciar_sesion_post'),
    path('registrarse/', views.registrarse_view, name='registrarse_view'),
    path('registrase_post', views.registrarse_post, name="registrarse_post"),
    path('cerrar/', views.cerrar_sesion, name='cerrar_sesion'),
    # Home de administrador y ciudadano
    path('administrador/', views.pagina_administrador_view, name="pagina_administrador_view"),
    path('ciudadano/', views.pagina_ciudadano_view, name="pagina_ciudadano_view"),
    # Requerimiento 4
    path('CambiarDatosCuentaP/', views.CambiarDatosCuentaP_view, name='CambiarDatosCuentaP'),
    path('CambiarDatosCuentaPOSTP/<int:id_user>', views.CambiarDatosCuentaPOSTP, name='CambiarDatosCuentaPOSTP'),
    path('CambioExitosoP/', views.CambioExitosoP_view, name='CambioExitosoP'),
    path('ErrorCambioDatosP', views.ErrorCambioDatosP_view, name='ErrorCambioDatosP'),
    # Requerimiento 5
    path('CrearPartidoPoliticoP/', views.CrearPartidoPoliticoP_view, name='CrearPartidoPoliticoP_view'),
    path('CrearPartidoPoliticoFormP/', views.CrearPartidoPoliticoFormP_view, name='CrearPartidoPoliticoFormP'),
    path('CrearPartidoPoliticoPOSTP/', views.CrearPartidoPoliticoPOSTP, name='CrearPartidoPoliticoPOSTP'),
    # Requerimiento 6
    path('ConsultarListaPartidosPoliticosAP/', views.ConsultarListaPartidosPoliticosAP_view, name='ConsultarListaPartidosPoliticosAP_view'),
    path('ConsultarListaPartidosPoliticosCP/', views.ConsultarListaPartidosPoliticosCP_view, name='ConsultarListaPartidosPoliticosCP_view'),
    # Requerimiento 7
    path('ConsultarPartidoPoliticoSAR/',views.ConsultarPartidoPoliticoSAR_view, name= 'ConsultarPartidoPoliticoSAR_view'),
    path('ConsultarPPSAR',views.ConsultarPPSAR_post, name= 'ConsultarPPSAR_post'),
    # Requerimiento 8
    path('administrador/Crear',views.CrearIndividuoASAR_view, name= 'CrearIndividuoASAR_view'),
    path('administrador/CrearIndividuo',views.CrearIndividuoASAR_post, name= 'CrearIndividuoASAR_post'),
    path('ciudadano/Crear',views.CrearIndividuoCSAR_view, name= 'CrearIndividuoCSAR_view'),
    path('ciudadano/CrearIndividuo',views.CrearIndividuoCSAR_post, name= 'CrearIndividuoCSAR_post'),
    path('CreacionExitosa/', views.CreacionExitosa_view, name='CreacionExitosa_view'),
    path('CreacionPendiente/', views.CreacionPendinte_view, name='CreacionPendiente_view'),
    # Requerimiento 9
    path('administrador/AprobarIndividuo',views.AprobarIndividuoSAR_view, name= 'AprobarIndividuoSAR_view'),
    path('administrador/AprobarIndividuoSAR',views.AprobarIndividuoSAR_post, name= 'AprobarIndividuoSAR_post'),
    path('AprobarExitoso/', views.AprobarExitoso_view, name='AprobarExitoso_view'),
    # Requerimiento 10
    path('ConsultarListaIndiCP', views.ConsultarListaIndiCP_view, name = 'ConsultarListaIndiCP_view'),
    path('ConsultarListaIndiAP', views.ConsultarListaIndiAP_view, name = 'ConsultarListaIndiAP_view'),
    # Requerimiento 11
    path('ConsultarIndividuo', views.ConsultarIndividuo_view, name = 'ConsultarIndividuo_view'),
    path('ConsultarIndividuoP', views.ConsultarIndividuo_post, name = 'ConsultarIndividuo_post'),
    # Requerimiento 12
    path('administrador/AfiliarIndividuo', views.AfiliarIndividuoASAR_view, name = 'AfiliarIndividuoASAR_view'),
    path('ciudadano/AfiliarIndividuo', views.AfiliarIndividuoCSAR_view, name = 'AfiliarIndividuoCSAR_view'),
    path('administrador/AfiliarIndividuoP', views.AfiliarIndividuoASAR_post, name = 'AfiliarIndividuoASAR_post'),
    path('ciudadano/AfiliarIndividuoP', views.AfiliarIndividuoCSAR_post, name = 'AfiliarIndividuoCSAR_post'),
    # Requerimiento 13
    path('administrador/AprobarAfiliacion',views.AprobarAfiliacionSAR_view, name= 'AprobarAfiliacionSAR_view'),
    path('administrador/AprobarAfiliacionSAR',views.AprobarAfiliacionSAR_post, name= 'AprobarAfiliacionSAR_post'),
    # Requerimiento 14
    path('administrador/CrearProceso', views.CrearProcesoASAR_view, name = 'CrearProcesoASAR_view'),
    path('ciudadano/CrearProceso', views.CrearProcesoCSAR_view, name = 'CrearProcesoCSAR_view'),
    path('administrador/CrearProcesoP', views.CrearProcesoASAR_post, name = 'CrearProcesoASAR_post'),
    path('ciudadano/CrearProcesoP', views.CrearProcesoCSAR_post, name = 'CrearProcesoCSAR_post'),
    # Requerimiento 15
    path('administrador/AprobarProceso',views.AprobarProcesoASAR_view, name= 'AprobarProcesoASAR_view'),
    path('administrador/AprobarProcesoSAR',views.AprobarProcesoASAR_post, name= 'AprobarProcesoASAR_post'),
    # Requerimiento 16
    path('administrador/ImplicarAfiliado', views.ImplicarAfiliadoASAR_view, name = 'ImplicarAfiliadoASAR_view'),
    path('ciudadano/ImplicarAfiliado', views.ImplicarAfiliadoCSAR_view, name = 'ImplicarAfiliadoCSAR_view'),
    path('administrador/ImplicarAfiliadoP', views.ImplicarAfiliadoASAR_post, name = 'ImplicarAfiliadoASAR_post'),
    path('ciudadano/ImplicarAfiliadoP', views.ImplicarAfiliadoCSAR_post, name = 'ImplicarAfiliadoCSAR_post'),
    # Requerimiento 17
    path('ConsultarProceso', views.ConsultarProceso_view, name = 'ConsultarProceso_view'),
    path('ConsultarProcesoP', views.ConsultarProceso_post, name = 'ConsultarProceso_post'),
    # Requerimiento 18
    path('administrador/Habilitar-Deshabilitar',views.HabDesSAR_view, name= 'HabDesSAR_view'),
    path('administrador/HABDES',views.HabDesSAR_post, name= 'HabDesSAR_post'),
    path('HABDESExitoso/', views.HabDesEXI_view, name='HabDesEXI_view'),

    path('acerca/',views.acerca_view, name= 'acerca'),
    path('usuarios', views.usuarios_view, name='usuarios_view'),
    path('ErrorCuenta', views.ErrorCuenta_view, name='ErrorCuenta'),
    #path('error_registro', views.error_registro_view, name="error_registro_view")
]





