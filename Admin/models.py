from django.db import models

# Create your models here.
   
class DB_Career(models.Model):
    full_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=254,null=True)
    mobile=models.CharField( max_length=250,null=True)
    resume=models.FileField( upload_to="Resume", max_length=100,null=True)
    date=models.DateTimeField(auto_now=True, auto_now_add=False, editable=True)

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date=models.DateTimeField(auto_now=True, auto_now_add=False,null=True, editable=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"