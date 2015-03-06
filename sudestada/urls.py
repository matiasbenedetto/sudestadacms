from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sudestada.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^redactor/', include('redactor.urls')),

    url(r'^$', 'revista.views.index', name='index'),

    url(r'^articulo/(?P<id_articulo>\d+)/(?P<slug>[-\w]+)/$', 'revista.views.articulo', name='articulo'),
    url(r'^edicion/(?P<id_edicion>\d+)/(?P<slug>[-\w]+)/$', 'revista.views.edicion', name='edicion'),
    url(r'^coleccion/(?P<id_coleccion>\d+)/(?P<slug>[-\w]+)/$', 'revista.views.coleccion', name='coleccion'),
    url(r'^seccion/(?P<slug>[-\w]+)/$', 'revista.views.seccion', name='seccion'),

    url(r'^comprar/$', 'revista.views.comprar', name='comprar'),
    url(r'^contacto/$', 'revista.views.contacto', name='contacto'),

    (r'^info/', include('django.contrib.flatpages.urls')),

    #migrando url viejas
    url(r'^article.php3/$', 'revista.views.articulo_migrar', name='articulo_migrar'),
    url(r'^web06/article.php3?/$', 'revista.views.articulo_migrar', name='articulo_migrar'),
    url(r'^bestiario.php3/$', 'revista.views.edicion_migrar', name='edicion_migrar'),
    url(r'^web06/bestiario.php3/$', 'revista.views.edicion_migrar', name='edicion_migrar'),
    url(r'^web06/$', 'revista.views.index_migrar', name='index_migrar'),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))