from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def admin_dashboard(request):
     enquiry_count=Enquiry.objects.all().count()
     career_count=DB_Career.objects.all().count()
     return render(request,'admin_dashboard.html',{'enquiry_count':enquiry_count,'career_count':career_count})

 
# Create your views here.
def enquiry_list(request):
     rec=Enquiry.objects.select_related().order_by('-id') 
     return render(request,'enquiry_list.html',{'rec':rec})
 # Create your views here.

def enquiry_details(request,id):
     data=Enquiry.objects.get(id=id) 
     return render(request,'enquiry_details.html',{'data':data})
 

def enquiry_form(request):
    if request.method == "POST":
        fm = EnquiryForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Thank you. We will contact you soon!')
            return redirect('/')
        else:
            messages.error(request, 'Form Not Submited')
            return redirect('/')
    else:
            messages.error(request, 'Form Not Submited')
            return redirect('/')

def delete_enquiry(request,id): 
    pi=Enquiry.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('/admin/enquiry_list',)
   


# Create your views here.
def career_list(request):
     rec=DB_Career.objects.select_related().order_by('-id') 
     return render(request,'career_list.html',{'rec':rec})

def delete_career(request,id): 
    pi=DB_Career.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('/admin/career_list',)
   

def career_form(request):
    if request.method == "POST":
        fm = CareerForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Thank you. We will contact you soon!')
            return redirect('/')
        else:
            messages.error(request, 'Form Not Submited')
            return redirect('/')
    else:
            messages.error(request, 'Form Not Submited')
            return redirect('/')

