from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# home
class HomeView(TemplateView):
    template_name = 'funcionario/home.html'

# Painel (protegido)
class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/painel.html'

# perfil (protegido)
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/perfil.html'