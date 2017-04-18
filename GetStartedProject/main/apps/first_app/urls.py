print "I will be your future routes; HTTP requests will be captured by me."

from django.conf.urls import url

def index():
	print ('8'*100)
	print ("bannnaananananaapeel")

urlpatterns = [
    url(r'^$', index)
]