from django.shortcuts import render
from django.http import HttpResponse
#from .models import LoginData
from .forms import LoginForm




# Create your views here.

def index(request):
    return render(request, 'pages/index.html')



def loginView(request):
        
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
       # username = request.POST.get('username')
       # password = request.POST.get('password')

        #if request.method == 'POST':
           #login_instance = LoginData(username=username, password=password)
           #login_instance.save()


        return render(request, 'pages/login.html',{"form":LoginForm})



def contact(request):
        return render(request, 'pages/contact.html')


    

def about(request):
        return render(request, 'pages/about.html')

def admin(request):
        return render(request, 'admin')

