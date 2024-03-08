from django import forms
from .models import Enquiry,DB_Career

class EnquiryForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom_message_style'}))
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'mobile', 'email', 'subject', 'message']

class CareerForm(forms.ModelForm):
    class Meta:
        model = DB_Career
        fields = ['full_name', 'email', 'mobile', 'resume']
