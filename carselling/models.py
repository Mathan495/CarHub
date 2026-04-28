from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename= "%s%s"%(now_time,filename)
    return os.path.join('uploads/', new_filename)

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=getfilename, blank=True, null=True)
    description= models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=getfilename, null=True, blank=True, default="default.png")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    quantity = models.IntegerField(null=False, blank=False) 
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=False, blank=False)
    trending=models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
class TestDrive(models.Model):
    product= models.ForeignKey('Car',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile= models.CharField(max_length=10)
    email=models.EmailField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
class Contact(models.Model):
    name= models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    message= models.CharField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 