from django.shortcuts import render, HttpResponse
import time

# Create your views here.
def index(request):
	context = {
	"somedate": theDate(),
	"sometime": theClock()
	}
	return render(request, "timedisplay/index.html", context)

def theDate():
	page_time= time.strftime('%b %d, %Y',time.localtime(time.time()))
	# page_time = timestrftime('')
	return page_time
def theClock():
	page_date= time.strftime('%I:%M:%S %p',time.localtime(time.time()))
	return page_date
