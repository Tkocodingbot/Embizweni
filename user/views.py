from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login



class signupuser(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request, 'user/UserRegistration.html', locals())
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'user/UserRegistration.html', locals())

# def signupuser(request):

#     if request.method =='GET':
#         return render(request, 'user/UserRegistration.html', {'form':UserRegistrationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)      # import login using django confi.auth to enable user to login after registration
#                 return redirect('home')
#             except IntegrityError:
#                 return render (request, 'user/UserRegistration.html', {'form':UserRegistrationForm(),'error':'Username already taken :(    please choose new username'})

#         else:
#             return render (request, 'user/UserRegistration.html', {'form':UserRegistrationForm(),'error':'Password did not match !!'})
