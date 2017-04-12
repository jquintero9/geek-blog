from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PerfilForm
#from django.contrib.auth.models import User
from .models import Perfil

# Create your views here.


class PerfilUsuario(LoginRequiredMixin, View):

    template_name = 'usuarios/perfil.html'
    login_url = reverse_lazy('account_login')

    def get(self, request):

        context = {}

        if Perfil.objects.filter(usuario=request.user).exists():
            perfil_usuario = Perfil.objects.get(usuario=request.user)
            context = {'perfil': perfil_usuario}

        return render(request, self.template_name, context)


class CrearPerfil(LoginRequiredMixin, CreateView):

    model = Perfil
    form_class = PerfilForm
    template_name = 'usuarios/perfil_form.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('usuario:perfil')

    def post(self, request, *args, **kwargs):
        request.POST['usuario'] = str(request.user.id)

        return super(CrearPerfil, self).post(request, *args, **kwargs)
