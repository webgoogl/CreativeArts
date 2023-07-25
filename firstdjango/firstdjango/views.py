from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import userform
from service.models import Services
from django.core.paginator import Paginator
from contactquery.models import query

def homePage(request):
    SD=Services.objects.all()
    paginator=Paginator(SD,5)
    page_number=request.GET.get('page')
    servicefinal=paginator.get_page(page_number)
    if request.method=="GET":
        st=request.GET.get('search_item')
        if st!=None:
            SD=Services.objects.filter(service_icon__icontains=st)

    data={
        'serviceData':servicefinal
    }
    return render(request,"start.html",data)

#process of saving user data into database
def saveQuery(request):
    if request.method=="POST":
        name=request.POST.get('username')
        number=request.POST.get('contacts')
        en=query(username=name,usernumber=number)
        en.save()
    return render(request,"aboutus.html")
#process of saving user data into database

def aboutus(request):
    return render(request,"aboutus.html")

def hello(request):
    return HttpResponse("Hello its my first time ")

def courseDetail(request,courseid):
    return HttpResponse(courseid)

def pricing(request):
    return render(request,"pricing.html")

def form(request):
    final=0;
    data={}
    fn=userform()
    data={"form":fn}
    try:
        if request.method =="POST":
            n1=int(request.POST.get("n1"))
            if n1%2==0:
                final="Even"
            else:
                final="Odd" 
            
            
            
    except:
        pass
    data={"c":final}
    return render(request,'form.html',data)