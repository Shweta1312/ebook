from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    year = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    
    def __str__(self):
        return self.year


class Subject(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_logo = models.FileField()
    sub_title = models.CharField(max_length=100)
      
    
    def __str__(self):
        return self.sub_title

class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    author= models.CharField(max_length=100)
    book_logo= models.FileField()
    book_title= models.CharField(max_length=200)
    book_detail=models.CharField(max_length=1000)
    book= models.FileField(blank= True,null=True,upload_to="static/homepage/")
      
    def __str__(self):
        return self.book_title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image= models.FileField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)