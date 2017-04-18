from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^process/message$', views.message),
	url(r'^process/comment/(?P<id>\d+)$', views.comment),

]
