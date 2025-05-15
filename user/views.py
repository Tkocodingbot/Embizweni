
from django.shortcuts import render,redirect

from user.models import Profile
from .forms import UserProfileForm, UserRegistrationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required




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

# Profile Class
# @login_required
class ProfileView(View):
    def get(self,request):
        form = UserProfileForm()
        return render(request, 'user/Profile.html', locals())
    def post(self,request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            province = form.cleaned_data['province']
            postal_code = form.cleaned_data['postal_code']
            
            reg = Profile(user=user,name=name,city=city,mobile=mobile,province=province,postal_code=postal_code)
            reg.save()
            messages.success(request, "Congradulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'user/Profile.html', locals())
    
def address(request):
    add = Profile.objects.filter(user=request.user)
    return render(request, 'user/address.html', locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add = Profile.objects.get(pk=pk)
        form = UserProfileForm(instance=add)
        return render(request, 'user/UpdateAddress.html', locals())
    def post(self,request,pk):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            add = Profile.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.province = form.cleaned_data['province']
            add.postal_code = form.cleaned_data['postal_code']
            add.save()
            messages.success(request, "Congradulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")
    
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
