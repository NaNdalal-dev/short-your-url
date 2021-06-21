from django.shortcuts import render
from pyshorteners import Shortener
from pyshorteners.exceptions import BadURLException

def home(request):
	tiny_url = None
	error = None
	if request.POST:
		try:
			url = Shortener()	
			tiny_url = url.tinyurl.short(request.POST['url'])
			
		except BadURLException:
			error = "Invalid URL."
		except:
			error = "Oops!! Something Went wrong."

	return render(request,'main.html',{'url':tiny_url,'error':error})