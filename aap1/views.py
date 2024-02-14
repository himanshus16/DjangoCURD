from django.shortcuts import render,HttpResponseRedirect
from .models import student
import os
 
def f1(req):
    return render(req,"app1/index.html")
def f2(req):
    if req.method=='POST':
        print(req.POST)
        fn=req.POST.get('fn')
        ln=req.POST.get('ln')
        age=req.POST.get('age')
        email=req.POST.get('email')
        image=req.FILES.get('img')
        data=student(name=fn,lname=ln,age=age,email=email,img=image)
        data.save()
    return render(req,"app1/insert.html")
def f3(req):
    head="This Data is Dynamically Updated"
    d=student.objects.all()
    return render(req,"app1/display.html",{'d1':head,'data':d})
def f4(req,pk):
    s=student.objects.get(id=pk)
    if req.method=="POST":
        fn=req.POST.get('fn')
        ln=req.POST.get('ln')
        age=req.POST.get('age')
        email=req.POST.get('email')
        image=req.FILES.get('img')
        user=student.objects.filter(pk=pk).update(name=fn,lname=ln,age=age,email=email,img=image)
        return HttpResponseRedirect("/display/",user)
    u=student.objects.get(pk=pk)
    return render(req,"app1/update.html",{"data":u})
def f5(req,n):
    data=student.objects.get(pk=n)
    # data=student.objects.get(id=n)         ("id": it refers to primary key it can be any key name like [name,age,email])
    data.delete()
    return HttpResponseRedirect("/display/")











# if len(req.FILES) != 0:
#     if len(student.img.url) > 0:
# s=student.objects.get(pk=pk)
# os.remove(s.img.path)
# user.save()