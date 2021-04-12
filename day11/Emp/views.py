from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/home.html')
def about(request):
    return render(request,'html/about.html')
def contact(request):
    return render(request,'html/contact.html')	
def login(request):
    return render(request,'html/login.html') 
def register(request):
	if request.method == "POST":
		u = request.POST['uname']
		e = request.POST['eml']
		a = request.POST['ag']
		p = request.POST['pd']
		d = {'usn':u,'emi':e,'age':a,'pwd':p}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')