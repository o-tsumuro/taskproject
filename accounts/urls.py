from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),

    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('logout/',
         auth_views.LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
         name='logout'),
    
    path('login_guest/',
         views.GuestUserView.as_view(),
         name='login_guest'),

]