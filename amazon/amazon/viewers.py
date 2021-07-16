from django.http import HttpResponse

def home(request):
    print("Entering home page")
    return HttpResponse("Welcome to home page")

def about_us(request):
    print("Entering aboutUs page")
    return HttpResponse("Welcome to aboutUs page")

def contact_us(request):
    print("Entering contactUs page")
    return HttpResponse("Welcome to contactUs page")