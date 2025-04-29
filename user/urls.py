from django.urls import path 
from user import views
from django.contrib.auth import views as auth_view  # This line code code is used to auto create login form, withouth writing views code. base on sugnup form that already exists.
from .forms import LoginForm

urlpatterns = [
    path('signup/', views.signupuser.as_view(), name='signupuser'),
    #path('signup/', views.signupuser, name="signupuser"),
    path ('accounts/login', auth_view.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm), name='login')
]
