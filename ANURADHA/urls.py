"""BPS URL Configuration

The `urlpatterns` list routes URLs to Web_views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function Web_views
    1. Add an import:  from my_app import Web_views
    2. Add a URL to urlpatterns:  path('', Web_views.home, name='home')
Class-based Web_views
    1. Add an import:  from other_app.Web_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from Web import views as Web_views
from Admin import views as Admin_views
from Admin import urls as AdminUrls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include(AdminUrls)),
    path('', Web_views.index,name="index"),
    path('enquiry_form/', Admin_views.enquiry_form, name="enquiry_form"), 
    path('career_form/', Admin_views.career_form, name="career_form"), 
    path('contact_us/', Web_views.contact_us, name="contact_us"), 
    path('career/', Web_views.career, name="career"), 

    path('set_session_exit_for_enquiry_form/', Web_views.set_session_exit_for_enquiry_form, name="set_session_exit_for_enquiry_form"), 

    # About Links 
    path('alumni/', Web_views.alumni,name="alumni"),
    path('tatya_saheb_message/', Web_views.tatya_saheb_message,name="tatya_saheb_message"),
    path('principal_message/', Web_views.principal_message,name="principal_message"),
    path('founder_message/', Web_views.founder_message,name="founder_message"),
    path('school_info/', Web_views.school_info,name="school_info"),
    path('vision_and_mission/', Web_views.vision_and_mission,name="vision_and_mission"),
    path('school_location/', Web_views.school_location,name="school_location"),
    path('phylosophy/', Web_views.phylosophy,name="phylosophy"),
    path('chikhli_city/', Web_views.chikhli_city,name="chikhli_city"),

    # General Informations Links
    path('teaching_staff/', Web_views.teaching_staff,name="teaching_staff"),
    path('School Times/', Web_views.school_times,name="school_times"),
    path('Important Days/', Web_views.important_days,name="important_days"),
    path('Calender/', Web_views.calender,name="calender"),
    path('Uniforms/', Web_views.uniform,name="uniform"),
    path('Rules/', Web_views.rules,name="rules"),
    path('Parent Meets/', Web_views.parents_meet,name="parents_meet"),
    path('Parents Consent Form/', Web_views.parents_consent_form,name="parents_consent_form"),

    # Admission Links 
    path('age_criteria/', Web_views.age_criteria,name="age_criteria"),
    path('documents/', Web_views.documents,name="documents"), 
    path('guidlines/', Web_views.guidlines,name="guidlines"),
    path('withdrawal/', Web_views.withdrawal,name="withdrawal"),

    # Academics Links
    path('crriculum/', Web_views.crriculum,name="crriculum"),
    path('co_crriculum/', Web_views.co_crriculum,name="co-crriculum"),

    # Facilities Links
    path('infrastucture/', Web_views.infrastructure,name="infrastructure"),
    path('hostel/', Web_views.hostel,name="hostel"),
    path('library/', Web_views.library,name="library"),
    path('computer_lab/', Web_views.computer_lab,name="computer_lab"),
    path('smart_classes/', Web_views.smart_classes,name="smart_classes"),
    path('news_papper/', Web_views.news_papper,name="news_papper"),
    path('transportations/', Web_views.transportation,name="transportations"),

    # Gallary Links
    path('photos/', Web_views.photos,name="photos"),
    path('videos/', Web_views.videos,name="videos"),

    # admin login links
    path('login/', Web_views.videos, name="login"),
    path('logout/', Web_views.videos, name="logout"),
    path('admin_home/', Web_views.videos, name="admin_home"),

    # Export Links
    path('export_enquiry/', Web_views.videos, name="export_enquiry"),

    # Other links


    path('alumni_form/',Web_views.videos, name='alumni_form'),
    path('alumni_list/',Web_views.videos, name='alumni_list'), 
    path('delete_alumni/<int:id>/',Web_views.videos, name='delete_alumni'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    