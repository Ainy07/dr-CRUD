from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from . models import Doctor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ragistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        image = request.FILES.get('image')
        password = make_password(request.POST.get('password'))
        category=request.POST.get('category')
        if Doctor.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return redirect("/")
        elif Doctor.objects.filter(contact=contact).exists():
            messages.error(request,'contact already exists')
            return redirect("/")
        else:
            Doctor.objects.create(name=name,degree=degree,email=email,contact=contact,
                                  password=password,category=category,image=image)
            return redirect("/login/")


def login(request):
    return render(request, 'Login.html')                

def login_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Doctor.objects.filter(email=email).exists():
            obj = Doctor.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect("/table/")
            else:
                return HttpResponse('password incorrect')
    else:
        return HttpResponse("phone number is not registered")
        
        
        
def table(request):
    data = Doctor.objects.all()
    return render(request, 'table.html', {"data": data})

# create edit button


def update_view(request, uid):
    res = Doctor.objects.get(id=uid)
    return render(request, 'update.html', {'D': res})

# use update data


def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        degree = request.POST['degree']
        contact = request.POST['contact']
        email = request.POST['email']
        image = request.POST['image']
        category = request.POST['category']
        Doctor.objects.filter(id=uid).update(name=name, email=email,
                                           contact=contact, image=image,
                                           degree=degree,category=category)
        return redirect('/table/')

# create delete button


def delete(request, pk):
    use = Doctor.objects.filter(id=pk).delete()
    return redirect('/table/')       