from django.conf.urls import patterns, include, url
#from notaprofs import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'notaprofs.views.home', name='home'),
    url(r'^perfil/', 'notaprofs.views.perfil', name = 'perfil'),
    url(r'^top/', 'notaprofs.views.top', name = 'top'),
    url(r'^todos/', 'notaprofs.views.todos', name = 'todos'),
    url(r'^search/', 'notaprofs.views.search', name = 'search'),
    url(r'^oque/', 'notaprofs.views.oque', name = 'oque'),

    # Examples:
    # url(r'^$', 'notaprofs.views.home', name='home'),
    # url(r'^notaprofs/', include('notaprofs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
