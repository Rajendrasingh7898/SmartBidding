from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp2 import models as myapp2_models
from django.core.files.storage import FileSystemStorage
from.import models
from time import time


# Create your views here.

#middleware to check session for admin routes
def sessioncheckmyadmin_middleware(get_response):
	def middleware(request):
		if request.path=='/myadmin/' or request.path=='/myadmin/addcategory/' or request.path=='/myadmin/addsubcategory/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/manageuserstatus/':
			if request.session['sunm']==None or request.session['srole']!="admin":
				response = redirect('/Login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware

def adminhome(request):
    return render(request,'adminhome.html',{"sunm":request.session['sunm']})

def manageusers(request):
    userDetails=myapp2_models.Register.objects.filter(role='user')
    return render(request,'manageusers.html',{"userDetails":userDetails,"sunm":request.session['sunm']})


def manageuserstatus(request):
    status=request.GET.get("status")
    regid=request.GET.get("regid")
    
    if status=="block":
        myapp2_models.Register.objects.filter(regid=int(regid)).update(status=0)
        
    elif status=="verify":
        myapp2_models.Register.objects.filter(regid=int(regid)).update(status=1)
    else:
        myapp2_models.Register.objects.filter(regid=int(regid)).delete()       
    return redirect("/myadmin/manageusers/",{"sunm":request.session['sunm']})

def addcategory(request):
    if request.method=="GET":
        return render(request,"addcategory.html",{"output":"","sunm":request.session['sunm']})
    else:
        categoryname=request.POST.get("categoryname")
        categoryicon=request.FILES["categoryicon"]
        fs=FileSystemStorage()
        filename=fs.save(categoryicon.name,categoryicon)
        p=models.Category(categoryname=categoryname,categoryicon=filename)
        p.save()
        return render(request,"addcategory.html",{"output":"Category added successfullt ...!","sunm":request.session['sunm']})
    
def addsubcategory(request):
    clist=models.Category.objects.all() 
    print(clist)
    if request.method=="GET":
        return render(request,"addsubcategory.html",{"clist":clist,"output":"","sunm":request.session['sunm']})
    else:
        categoryname=request.POST.get("categoryname")
        subcategoryname=request.POST.get("subcategoryname")
        categoryicon=request.FILES["categoryicon"]
        fs=FileSystemStorage()
        filename=fs.save(categoryicon.name,categoryicon)
        p=models.subCategory(subcategoryname=subcategoryname,categoryname=categoryname,subcategoryicon=filename)
        p.save()
        return render(request,"addsubcategory.html",{"clist":clist, "output":"sub Category added successfullt ...!","sunm":request.session['sunm']})
    
    
def cpadmin(request):
 if request.method=="GET":  
  return render(request,"cpadmin.html",{"sunm":request.session['sunm'],"output":""})
 else: 
  opass=request.POST.get("opass")
  npass=request.POST.get("npass")   
  cnpass=request.POST.get("cnpass")
  sunm=request.session['sunm']

  userDetails=myapp2_models.Register.objects.filter(username=sunm,password=opass)
  if len(userDetails)>0:
    if npass==cnpass:
      myapp2_models.Register.objects.filter(username=sunm).update(password=cnpass)      
      return render(request,"cpadmin.html",{"sunm":request.session['sunm'],"output":"Password changed , please login again...."})
    else:
      return render(request,"cpadmin.html",{"sunm":request.session['sunm'],"output":"New & confirm new password not matched"})
  else:
    return render(request,"cpadmin.html",{"sunm":request.session['sunm'],"output":"Invalid old password , please try again"}) 

def epadmin(request):
  if request.method=="GET":
    sunm=request.session['sunm'] 
    userDetails=myapp2_models.Register.objects.filter(username=sunm)  
    m,f="",""
    if userDetails[0].gender=="male":
     m="checked"
    else:
      f="checked"
    return render(request,"epadmin.html",{"sunm":request.session['sunm'],"output":"its working","userDetails":userDetails[0],"m":m,"f":f})   
      
  else:
    name=request.POST.get("name")
    username=request.POST.get("username")           
    mobile=request.POST.get("mobile")
    address=request.POST.get("address")
    city=request.POST.get("city")
    gender=request.POST.get("gender")

  myapp2_models.Register.objects.filter(username=username).update(name=name,mobile=mobile,address=address,city=city,gender=gender)   

  return redirect("/myadmin/epadmin/")    


def addproducts(request):
  sclist=models.subCategory.objects.filter()
  if request.method=="GET":
    return render(request,"addproducts.html",{"sunm":request.session['sunm'],"output":"","sclist":sclist})
  else:
    atitle=request.POST.get("atitle")
    acategory=request.POST.get("acategory")   
    adescription=request.POST.get("adescription")
    baseprice=request.POST.get("baseprice")
    info=time()

    p=models.Addproduct(atitle=atitle,acategory=acategory,adescription=adescription,baseprice=baseprice,info=info)  
    p.save()

    return render(request,"addproducts.html",{"sunm":request.session['sunm'],"output":"Product added for Auction","sclist":sclist})        