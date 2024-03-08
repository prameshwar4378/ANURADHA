from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from urllib import response
from Admin.forms import *
from django.http import JsonResponse
# Create your views here.

# def all_enquiry(request):
#     list=DB_Enqueries.objects.all()
#     rec=DB_Enqueries.objects.order_by('-id')
#     count=rec.count()
#     data={'count':"count"}
#     return render(request,"admin_panel/enquiry_list.html",data)
    
def set_session_exit_for_enquiry_form(request): 
    request.session['is_session_exit_for_enquiry_form']=True
    request.session.set_expiry(5 * 24 * 60 * 60)  #5 days notification will hide
    return redirect('/')
    
def index(request): 
    fm=EnquiryForm()
    is_session_exit = request.session.get('is_session_exit_for_enquiry_form', False)
    return render(request,'index.html',{'fm':fm,'is_session_exit':is_session_exit})
    
def contact_us(request):
    fm=EnquiryForm()
    return render(request,'contact_us.html',{'fm':fm})
    
def career(request): 
    fm=CareerForm()
    return render(request,'career.html',{'fm':fm})
    
def alumni(request):
    return render(request,'about/alumni.html')

def tatya_saheb_message(request):
    return render(request,'about/tatya_saheb_message.html')
    
def founder_message(request):
    return render(request,'about/founder_message.html')
    
def principal_message(request):
    return render(request,'about/principal_message.html')
    
def school_info(request):
    return render(request,'about/school_info.html')

def vision_and_mission(request):
    return render(request,'about/vision_and_mission.html')
    
def school_location(request):
    return render(request,'about/location.html')
        
def phylosophy(request):
    return render(request,'about/phylosophy.html')
           
def chikhli_city(request):
    return render(request,'about/chikhli_city.html')
    

# General Informations Links

def teaching_staff(request):
    return render(request,'general_info/teaching_staff.html')
    
def school_times(request):
    return render(request,'general_info/school_times.html')
     
def important_days(request):
    return render(request,'general_info/important_days.html')
        
def calender(request):
    return render(request,'general_info/calender.html')
        
def uniform(request):
    return render(request,'general_info/uniform.html')
        
def rules(request):
    return render(request,'general_info/rules.html')
        
def parents_meet(request):
    return render(request,'general_info/parents_meet.html')
        
def parents_consent_form(request):
    return render(request,'general_info/parents_consent_form.html')


#   Admission Section     
def age_criteria(request):
    return render(request,'admission/age_rules.html')
        
def documents(request):
    return render(request,'admission/documents.html')
      
def guidlines(request):
    return render(request,'admission/guidlines.html')
        
def withdrawal(request):
    return render(request,'admission/withdrawal.html')


    #  Academics Section     
def crriculum(request):
    return render(request,'academics/crriculum.html')
              
def co_crriculum(request):
    return render(request,'academics/co-crriculum.html')

    # Facilities Section
def infrastructure(request):
    return render(request,'facilities/infrastructure.html')

def hostel(request):
    return render(request,'facilities/hostel.html')

def library(request):
    return render(request,'facilities/library.html')

def computer_lab(request):
    return render(request,'facilities/computer_lab.html')

def smart_classes(request):
    return render(request,'facilities/smart_classes.html')

def news_papper(request):
    return render(request,'facilities/news_papper.html')

def transportation(request):
    return render(request,'facilities/transportation.html')


    # Gallary Section
    
def photos(request):
    return render(request,'gallary/photos.html')
    
def videos(request):
    return render(request,'gallary/videos.html')



def admin_login(request):
    return render(request,'admin_panel/admin_login.html')

# @login_required(login_url='/login')
# def admin_home(request):
#     career_var=DB_Career.objects.order_by('-id')
#     career_count=career_var.count()

#     enquiry_var=DB_Enqueries.objects.order_by('-id')
#     enquiry_count=enquiry_var.count()
#     data={'career_count':career_count,'enquiry_count':enquiry_count}  
#     return render(request,'admin_panel/admin_home.html',data)




# from .forms import Alumni_form, login_form, Enquiry_form, Career_form
# from django.contrib.auth import authenticate,login,logout
# from django.shortcuts import redirect, render,get_object_or_404
# from django.contrib import messages



   
# def enquiry_form(request):
#     fm=EnquiryForm()
#     if request.method=="POST":
#         fm=EnquiryForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request,'Thank You. We will contact you soon ...!')
#             return redirect('/enquiry_form')
#     return render(request,'admin_panel/enquiry_form.html',{'fm':fm,'name':"rameshwar"})
  
# def enquiry_list(request):

#     rec=DB_Enqueries.objects.order_by('-id')
#     count=rec.count()
#     data={'rec':rec,'count':count}     
#     return render(request,"admin_panel/enquiry_list.html",data) 


# def delete_enquiry(request,id):
#     if request.method=='POST':
#         rm=Enquiry_form(request.POST)
#         pi=DB_Enqueries.objects.get(pk=id)
#         pi.delete()
#         messages.success(request,'Record Deleted Successfully')
#     return redirect('/enquiry_list',{'pi':pi})

# def resolve_enquiry(request,id):

#     if request.method=="POST":
#         pi=DB_Enqueries.objects.get(pk=id)
#         fm=Enquiry_form(request.POST,request.FILES, instance=pi)
        
#         if fm.is_valid():
#             fm.save()
#             fm=Enquiry_form()
#             messages.success(request,'Record Updated Successfully')
#         return redirect('/enquiry_list')
#     else:
#         pi=DB_Enqueries.objects.get(pk=id)
#         fm=Enquiry_form(instance=pi)
#     return render(request,'admin_panel/resolve_enquiry.html',{'fm':fm,'rec':pi})


# def career_form(request):
#     fm=Career_form()
#     if request.method=="POST":
#         fm=Career_form(request.POST,request.FILES)
#         if fm.is_valid():
#             dt=fm.save(commit=False)
#             dt.save()
#             messages.success(request,'Record Created Successfully')
#             fm=Career_form() 
#     return render(request,"admin_panel/career_form.html",{'fm':fm})
 
# def career_list(request):
#     rec=DB_Career.objects.order_by('-id')
#     count=rec.count()
#     data={'rec':rec,'count':count}     
#     return render(request,"admin_panel/career_list.html",data) 



# def delete_career(request,id):
#     if request.method=='POST':
#         rm=Career_form(request.POST)
#         pi=DB_Career.objects.get(pk=id)
#         pi.delete()
#         messages.success(request,'Record Deleted Successfully')
#     return redirect('/career_list',{'pi':pi})




  

# def alumni_form(request):
#     fm=Alumni_form()
#     if request.method=="POST":
#         fm=Alumni_form(request.POST,request.FILES)
#         if fm.is_valid():
#             dt=fm.save(commit=False)
#             dt.save()
#             messages.success(request,'Record Created Successfully')
#             fm=Alumni_form() 
#     return render(request,"admin_panel/alumni_form.html",{'fm':fm})
 


# def alumni_list(request):
#     rec=DB_Alumni.objects.order_by('-id')
#     count=rec.count()
#     data={'rec':rec,'count':count}     
#     return render(request,"admin_panel/alumni_list.html",data) 



# def delete_alumni(request,id):
#     if request.method=='POST':
#         rm=Alumni_form(request.POST)
#         pi=DB_Alumni.objects.get(pk=id)
#         pi.delete()
#         messages.success(request,'Record Deleted Successfully')
#     return redirect('/alumni_list',{'pi':pi})







# def export_excel_enquiries(request):
#     record_resource = Enquiry_Resource()
#     dataset = record_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="Enquiries.xls"'
#     return response






# def admin_login(request):
#     form=login_form()
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/admin_home',{'user',user})
#         else:
#             form=login_form()
#             messages.error(request,'Opps...! User does not exist... Please try again..!')

#     return render(request,"admin_panel/admin_login.html",{'form':form})


# def admin_logout(request):
#     logout(request)
#     return redirect('/login')
