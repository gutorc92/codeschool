from django.conf.urls import url, include
from cs_auth import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url('^friends/$', views.friends, name='user-friends'),
    url(r'^', include('userena.urls', namespace=None)),
]
