from django.shortcuts import render,HttpResponse,redirect
from basicapp.forms import myform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from django.contrib.auth.models import User
from to_do.forms import TodoForm
from to_do.models import Todo
# Create your views here.
def index(request):
    form=myform()
    if request.method=='POST':
        form=myform(request.POST)
        if form.is_valid():
            pass1=form.cleaned_data['password']
            pass2=form.cleaned_data['confirmpassword']
            em=form.cleaned_data['email']
            if pass1==pass2:
              if User.objects.filter(email=em).exists():
                 messages.info(request,'email taken')
              else:
                use=form.save()
                use.set_password(use.password)
                use.save()
                return redirect('/')
            else:
              messages.info(request,'password not matching')
              return redirect('/register')
              


    return render(request,'index.html',{'form':form})

def home(request):
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('list/')
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("invalid details")
    
    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')