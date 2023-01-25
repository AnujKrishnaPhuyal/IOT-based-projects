from ast import IsNot
import email
from operator import is_not
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import data_model
from .forms import Signup_model, login_model
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User



# Create your views here.
@csrf_exempt
def incoming_data(request):
    
      if request.method=='POST':
        first=request.body
        var= json.loads(first)
        var1= (var[0]['temperature'])
        var2= (var[0]['pulse'])
        var3= (var[0]['oxygen'])
        print(var1)
        print(var2)
        print(var3)
        reg= data_model(temp=var1, pul=var2, oxy=var3)
        reg.save()
        print(reg.temp, reg.pul, reg.oxy)
        return HttpResponse("chalyo")
        

      else:
        # st= data_model.objects.all
        return render(request, 'second/home.html')
        
def disp_data(request):
    total = data_model.objects.all()
    print(total)
    return JsonResponse({"users":list(total.values())})

def table(request):
  return render(request,'second/table.html')   

@csrf_exempt 
def Signup(request):
    fm=Signup_model(request.POST)
    if fm.is_valid():
         fm.save()
         print("hello")
         return HttpResponseRedirect('/login/')
    else:
          fm=Signup_model()
    return render(request,'second/signup.html',{'form':fm})

@csrf_exempt      
def user_login(request):
  if request.method=="POST":    
    fm = login_model(request=request, data=request.POST)
    if fm.is_valid():
          uname= fm.cleaned_data['username']
          upass= fm.cleaned_data['password']
          user = authenticate(username = uname, password = upass)
          if user is not None:
                login(request,user)
                # return HttpResponseRedirect('/profile/')
                if request.user.is_authenticated:
                      if request.user.is_superuser == True:
                            user = User.objects.all()
                            return render(request, 'second/admin_profile.html',{'user':user, 'uname':uname})  
                      else:         
                        return render(request, 'second/profile.html',{"uname":uname})    

   
  else:
    fm=login_model()

  return render (request ,'second/login.html',{'form':fm})      




             
      
  #  if request.user.is_authenticated:
  #       if request.method == 'POST':
  #             if request.user.is_superuser == True:
  #                   user = User.objects.all()
  #             else:
  #                   user = None
  #       else:
  #         if request.user.is_superuser == True:
  #               user = User.objects.all()
  #         else:
  #           user=None 
  #       return render(request, 'second/profile.html',{'user':user})   

  #  else:
  #        return HttpResponseRedirect('/login/')
          
                
# def userdisp(request, id):
#    if request.user.is_authenticated:
#          pi = User.objects.get(pk=id)
#          return render(request, 'second/userdisp.html',{"pi":pi})

    
    
def blank(request):
      return  HttpResponseRedirect('/login/')

def disp_table(request):
      if request.user.is_authenticated:
             return render(request, 'second/disp_table.html',{"name":request.user})


def front_admin(request,id):
       if request.user.is_authenticated:
         pi = User.objects.get(pk=id)
         users = User.objects.all()
         return render(request, 'second/front_admin.html',{"pi":pi,"users":users})


def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')         

      
      
def admin_profile(request):
   if request.user.is_authenticated:
        user = User.objects.all()
        return render(request, 'second/admin_profile.html',{'user':user})
         
