from django.db import models
from django.core.validators import FileExtensionValidator


# class Student(models.Model):
#     reg_id = models.IntegerField()
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     gender = models.CharField(max_length=20)
#     cgpa = models.CharField(max_length=100)
#     branch = models.CharField(max_length=100)
#     email = models.EmailField(default="")
#     phone = models.IntegerField(null=True)
#     image = models.ImageField(upload_to='form_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.fname +" "+self.lname
    

class Payment(models.Model):
    name = models.CharField(max_length=100 ,blank=True)
    email = models.CharField(max_length=100)
    amount = models.CharField(max_length=25)
    fname = models.CharField(max_length=100, default="Artist")
    title = models.CharField(max_length=50, default="Artwork Title")
    # order_id = models.CharField(max_length=1000)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self.name   
    

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    markerTitle = models.CharField(max_length=100)  

    def __str__(self):
        return self.markerTitle


class Artwork(models.Model):
    email = models.EmailField(default="")
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    url = models.CharField(max_length=500)
    medium = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    price = models.CharField(max_length=25 , blank=True)
    image = models.ImageField(upload_to='form_images', null=True, blank=True)
    location = models.CharField(max_length=100)
    

    def __str__(self):
        return self.fname +" "+self.lname
    

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    



