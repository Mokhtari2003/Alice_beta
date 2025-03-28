from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate ,login ,logout
from .forms import UserAccountsForm

def account_login(request):
   username = request.POST["username"]
   password = request.POST["password"]

      
   user = authenticate(
         request,
         username=username,
         password=password
     )
   if user is not None:
      login(request ,user)
      print(user ,request.POST)
      return redirect("../")
   else :
      print("ridi" ,request ,user ,username , password)
      return redirect("/Register")
   

def Register(request):
   errors = None
   if request.method == "POST" :    
      if 'login' in request.POST  :
         ac_login = account_login(request)
         return ac_login
      else :
         signupform = UserAccountsForm(request.POST)
         if signupform.is_valid():
            password1 = signupform.cleaned_data.get("password")
            password2 = signupform.cleaned_data.get("password2")
            if password1 == password2:
               user = signupform.save(commit=False)  # ابتدا بدون ذخیره در دیتابیس
               user.set_password(password1)  # حالا رمز هش می‌شود
               user.save()  # ذخیره نهایی

               login(request ,user)
               return redirect("../")
            else:
               signupform.add_error('password2', "Passwords do not match")
               return redirect("./")
      errors = signupform.errors
               
         
            
   return render(request ,'Register/index.html' , {'signupform' : UserAccountsForm() , 'error' : errors})

def logout_views(request):
   if request.user.is_authenticated:
      logout(request)
   return redirect(".")


   
      
      