from django.shortcuts import render, redirect
from app_cad_usuarios.models import Usuario
from app_cad_usuarios.forms import UsuarioForm


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'form': form, 'usuarios': usuarios})