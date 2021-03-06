from django.views.generic import CreateView
from django.urls import reverse_lazy
from . forms import CustomUserCerationForm
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCerationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'