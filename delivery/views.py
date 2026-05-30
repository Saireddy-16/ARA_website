from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Dress
# Create your views here.

def index(request):
    return render(request,'index.html')

def open_signup(request):
    return render(request,'signup.html')

def open_signin(request):
    return render(request,'signin.html')

def signup(request):
    #return HttpResponse("recieved")
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
    try:
        Customer.objects.get(username=username)
        return HttpResponse("Username already exist,try another name...")
    except:
        Customer.objects.create(username = username,
                            email = email,
                            password = password,
                            mobile = mobile,
                            address = address)
        return render(request,"signin.html")

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        try:
            Customer.objects.get(email=email,password=password)
            if email == "ara225@gmail.com":
                return render(request,"admin_home.html")
            else:
                return render(request,"customer_home.html")
        except Customer.DoesNotExist:
            return render(request,"fail.html")
def open_add_dress(request):
    return render(request,"add_dress.html")
def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        photo = request.POST.get('photo')
        rating = request.POST.get('rating')
        details = request.POST.get('details')
        price = request.POST.get('price')
        Dress.objects.create(name = name,
                    photo = photo,
                    rating = rating,
                    details = details,
                    price = price)
        dresses = Dress.objects.all()
        return render(request,"show_dresses.html",{'dresses':dresses})

         