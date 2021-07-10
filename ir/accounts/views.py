from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Destination
import traceback
from django.core.files.storage import FileSystemStorage




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')        
def register(request):
    
            if request.method == "POST":
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password1 == password2:
                   if User.objects.filter(username=username).exists():
                       messages.info(request,'Username taken')
                       return redirect('register')
                   elif User.objects.filter(email=email).exists():
                       messages.info(request,'EMAIL taken')
                       return redirect('register')
                   else:    
                    user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                    user.save();
                    print("User created")
                    return redirect('login')
                else:
                 messages.info(request,'password not matching...')
                 return redirect('register')
            else :
                return render(request, 'register.html')
            
def logout(request):
    auth.logout(request)            
    return redirect('/')

def postdestination(request):
    if request.method == 'POST':
        try:
            f = request.FILES["img"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
            name = request.POST['name']
            # img = request.POST['img']
            description = request.POST['description']
            price = request.POST['price']
            offer = request.POST.get('offer')
            
            if offer == "on":
                offer = True
            else:
                offer = False
            
            d = Destination.objects.create(name=name, desc=description,img=uploaded_file_url,price=price,offer=offer)
            d.save()
        except  Exception as e:
            traceback.print_exc()
        return redirect('/')
    else:
        return render(request, 'post_destination.html')
            