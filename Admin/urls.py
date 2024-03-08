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
from django.urls import path,include
from django.conf.urls.static import static
from .views import *
urlpatterns = [ 
    path('', admin_dashboard,name="admin_dashboard"),
    path('enquiry_list/', enquiry_list,name="enquiry_list"),
    path('enquiry_details/<int:id>', enquiry_details,name="enquiry_details"),
    path('delete_enquiry/<int:id>', delete_enquiry,name="delete_enquiry"),
    path('career_list/', career_list,name="career_list"),
    path('delete_career/<int:id>', delete_career,name="delete_career"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    