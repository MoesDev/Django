from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/register$', views.register),
    url(r'^user/login$', views.login),
    url(r'^user/success/$', views.success),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
    url(r'^signout$', views.signout),
    url(r'^not_signed_in/$', views.not_signed_in),

]