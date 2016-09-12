from django.conf.urls import include, url

from contatos.views import *

urlpatterns = [
  # Examples:
  # url(r'^$', 'aprendiz.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^$', principal, name="principal"),
  url(r'^adicionar/', adicionar, name="adicionar"),
  url(r'^mostrar/(?P<id>\d+)', mostrar, name="par"),
  url(r'^apagar/(?P<id>\d+)', apagar, name="apagar"),
  url(r'^editar/(?P<id>\d+)', editar, name="editar"),
]