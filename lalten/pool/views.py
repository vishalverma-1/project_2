#----------create operation------------
from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import ninja
def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        obj=ninja.objects.create(name=name,age=age,email=email,mobile=mobile)
        obj.save()
        return redirect('read')
    else:
        return render(request,'create.html')
    
#-----------read or data show operation------------

def read(request):
    obj=ninja.objects.all()
    return render(request,'read.html',{'obj':obj})    
    

#------------DELETE OPERATION---------------


def delete(request,id):
    obj=ninja.objects.get(id=id)
    obj.delete()
    return redirect('read')


#------------EDIT OPERATION-------------

def edit(request,id):
    if request.method=='POST':
     name=request.POST['name']
     age=request.POST['age']
     email=request.POST['email']
     mobile=request.POST['mobile']
     obj=ninja.objects.filter(id=id).update(name=name,age=age,email=email,mobile=mobile)
     return redirect('read')
    else:
        data=ninja.objects.filter(id=id)
        return render(request,'edit.html',{'data':data})