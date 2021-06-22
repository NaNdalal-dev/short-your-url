from django.shortcuts import render
from pyshorteners import Shortener
from pyshorteners.exceptions import BadURLException

def home(request):
	tiny_url = None
	error = None
	original_url = None
	if request.POST:
		try:
			original_url = request.POST['url']
			url = Shortener()	
			tiny_url = url.tinyurl.short(original_url)
			
		except BadURLException:
			error = "Invalid URL."
		except:
			error = "Oops!! Something Went wrong."

	return render(request,'main.html',{
		'url':tiny_url,
		'error':error,
		'original_url':original_url})