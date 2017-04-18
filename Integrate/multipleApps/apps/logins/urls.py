from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/register$', views.register, name="register"),
    url(r'^user/login$', views.login, name="login"),
    url(r'^user/success/(?P<id>\d+)/$', views.success, name="success"),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name="delete"),

]