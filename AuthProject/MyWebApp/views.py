from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request,'MyWebApp/dashboard.html')
def help(request):
    return render(request,'MyWebApp/help.html')
def contact(request):
    return render(request,'MyWebApp/contact.html')
def home(request):
    return render(request,'MyWebApp/home.html')

def success(request):
    return render(request,'MyWebApp/success.html')

def register_user(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            messages.success(request,f"Hello { username }, Your Account is Created")
            return redirect('home')
        else:
            form = NewUserForm()
    form = NewUserForm()
    return render(request,'MyWebApp/register.html',{'register_form':form})
@login_required()
def profile(request):
    return render(request,'MyWebApp/profile.html')