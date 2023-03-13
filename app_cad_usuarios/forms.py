from django.forms import ModelForm
from app_cad_usuarios.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade']