from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Painel (protegido)
class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/painel.html'

# perfil (protegido)
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/perfil.html'