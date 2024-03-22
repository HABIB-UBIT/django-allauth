from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'allauth/index.html')

def dashboard(request):
    return render(request,'allauth/dashboard.html')