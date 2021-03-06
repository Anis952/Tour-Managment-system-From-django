
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Image
from .models import Contact, Booking
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models  import Image


#from .forms import CustomerRegistrationForm


# Create your views here.
def home(request):
	pics = Image.objects.all()
	if request.method=="POST":
		#contact.contact()
		 name=request.POST.get('name')
		 email=request.POST.get('email')
		 subject=request.POST.get('subject')
		 #contact.name=name
		 #contact.email=email
		 #contact.subject=subject
		 #Contact.save()
		 print(name, email, subject)
		 #contact = contact(name=name, email=email, subject=subject)
		 contact = Contact(name=name, email=email, subject=subject)
		 contact.save()

		 return HttpResponse("Thank you for your response, our team will catch you soon")
	return render(request, 'app/index.html', {"pics":pics})


def about(request):
    return render(request, 'app/about.html')

def booking(request):
	if request.method=="POST":
		#contact.contact()
		 travellingform=request.POST.get('travellingfrom')
		 travellingto=request.POST.get('travellingto')
		 departing=request.POST.get('departing')
		 returing=request.POST.get('returing')
		 adults=request.POST.get('adults')
		 childern=request.POST.get('children')
		 traveltypes =request.POST.get('traveltypes') 
		 print(travellingform, travellingto,  departing, returing,  adults, childern )
		 #contact = contact(name=name, email=email, subject=subject)
		 Booking1 = Booking(travellingform=travellingform,travellingto=travellingto, departing=departing, returing=returing,adults=adults,childern=childern,traveltypes=traveltypes)
		 Booking1.save()

		 return HttpResponse("Thank you for Booking, our team will catch you soon")
	return render(request, 'app/booking.html')

	
def detail(request, id):
	data= Image.objects.get(pk=id)
	
	return render(request, 'app/detail.html', {"data": data})


def uppermusta(request):
	return render(request, 'app/uppermusta.html')

	



def photo(request):
    return render(request, 'app/photo.html')

def customerregistration(request):
	if request.method =='POST':
		print("hello")
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			form =UserCreationForm()
	else:
		form = UserCreationForm()	
	return  render(request,'app/customerregistration.html', {'form':form})
    
def loginn (request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse("Thanks for Login")
		
		# form = AuthenticationForm(request=request,user=request.POST)
		# if form.is_valid():
		# 	usr = form.cleaned_data['username']
		# 	pwdd = form.cleaned_data['password']
		# 	userss = authenticate(username=usr,password=pwdd)
		# 	if userss is not None:
		# 		login(request, userss)
		# 		return HttpResponse("login success")

	
	form = AuthenticationForm()
	return render(request, 'app/login.html',{'form':form}) 

	
def search(request):
     query = request.GET['query']
     pics =Image.objects.filter(title__icontains=query)
     params={'pics': pics}
     return render(request,'app/search.html',params)




