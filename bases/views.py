from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url     = 'login'




