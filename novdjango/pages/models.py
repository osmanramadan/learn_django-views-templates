from django.db import models

# Create your models here.

class Female(models.Model):
    name= models.CharField(max_length=50,null=True, blank=True,verbose_name='Female Name')

    def __str__(self):
        return self.name

class  Male(models.Model):
    name= models.CharField(max_length=50,null=True, blank=True,verbose_name='Male Name')
    girlfriend= models.OneToOneField(Female, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class LoginData(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


    
