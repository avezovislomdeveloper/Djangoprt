from django.db import models

# Create your models here.


class MainImage(models.Model):
    name = models.CharField(max_length=10)
    main_image=  models.ImageField()
    
    def __str__ (self):
        return self.name
    
    
class SecondImage(models.Model):
    name= models.CharField(max_length=10)
    firt_image = models.ImageField()
    second_image = models.ImageField()
    third_image = models.ImageField()
    
    def __str__ (self):
        return self.name
    
    
class ThirdImage(models.Model):
    name = models.CharField(max_length=10)
    about_image = models.ImageField()
    
    def __str__ (self):
        return self.name