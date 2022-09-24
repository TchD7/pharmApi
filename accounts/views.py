from django.shortcuts import render,redirect
from dashbord.views import create
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate,login,logout

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('create')
        else:
            messages.error(request, "Vérifier les champs")
            return redirect('signin')
    return render(request, 'index.html')
def signout(request):
    logout(request)
    messages.success(request, "Déconnecté avec sucess")
    return redirect('signin')