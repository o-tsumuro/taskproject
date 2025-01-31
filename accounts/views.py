from django.views import generic
from django.views import View
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate 
from django.shortcuts import redirect
from .models import CustomUser

class SignUpView(generic.CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('accounts:login')
   template_name = 'signup.html'

   def form_valid(self, form):
      user = form.save()
      self.object = user
      return super().form_valid(form)

class GuestUserView(View):
   def get(self, request):
      if not request.session.session_key:
         request.session.create()
      request.session.set_expiry(0)
      guest_username = f"guest_{request.session.session_key}"
      user = CustomUser(username=guest_username)
      user.set_unusable_password()
      user.save()
      login(request, user)
      return redirect('taskapp:index')