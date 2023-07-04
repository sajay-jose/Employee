from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register
from.models import login

# Create your views here.
def display(request):
  return render(request,'register.html')
def reg(request):
  if request.method == 'POST':
    emp_id=int(request.POST['emp_id'])
    emp_name=request.POST['emp_name']
    emp_age=int(request.POST['emp_age'])
    username=request.POST['username']
    password=request.POST['password']  
    image=request.FILES['image']
    data=Register.objects.create(emp_id=emp_id,emp_name=emp_name,emp_age=emp_age,username=username,image=image)
    data.save()
    data1=login.objects.create(username=username,password=password)
    data1.save()
    return render(request,'register.html')
  else:
    return render(request,'register.html')

def profile(request):
  if 'id' in request.session:
    username=request.session['id']
    if request.method == 'GET':
      data= Register.objects.filter(username=username).all()
      return render(request,'profile.html',{'r': data})
  else:
    return redirect(log)
def log(request):
  if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    try:
      data=login.objects.get(username=username)
      if data.password == password:
        request.session['id'] = username  #session created
        return redirect(profile)
      else:
        return HttpResponse("password error")
    except Exception:
      return HttpResponse("username error")
  else:
    return render(request,'login.html')
def logout(request):   
  if 'id' in request.session:
    request.session.flush()
    return redirect(log)

def password(request):
  if request.method == 'POST':
    username=request.POST['username']
    old_password=request.POST['old_password']
    new_password=request.POST['new_password']
    data= login.objects.filter(username=username).update(new_password=new_password)
    return render(request,'register.html')
  else:
    return render(request,'change_password.html')

    