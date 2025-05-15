from django.urls import path 
from user import views
from django.contrib.auth import views as auth_view  # This line code code is used to auto create login form, withouth writing views code. base on sugnup form that already exists.
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm



urlpatterns = [
    path('signup/', views.signupuser.as_view(), name='signupuser'),
    #path('signup/', views.signupuser, name="signupuser"),
    path ('accounts/login', auth_view.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='user/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('UpdateAddress/<int:pk>', views.UpdateAddress.as_view(), name='UpdateAddress'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='user/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
]
