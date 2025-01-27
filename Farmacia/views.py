from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render

from Farmacia.forms import UsuarioForm
from Farmacia.models import Usuario


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'login.html')



def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})