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

def view(request, pk):
    data = {}
    data['usuarios'] = Usuario.objects.get(pk=pk)
    return render(request, 'usuarios/view.html', data)

def edit(request, pk):
    data = {}
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('view', pk=pk)
    else:
        form = UsuarioForm(instance=usuario)
    data['usuarios'] = usuario
    data['form'] = form
    return render(request, 'usuarios/edit.html', data)

def delete(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.delete()
    return redirect('home')