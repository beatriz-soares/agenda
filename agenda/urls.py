from django.conf.urls import include, url
from django.contrib import admin
from contatos.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'aprendiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', principal),
    url(r'^contatos/', include('contatos.urls')),
]
