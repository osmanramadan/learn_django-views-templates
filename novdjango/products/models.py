from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name='Product Name')
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=100,max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True,choices=[('phone','phone'),('laptop','laptop'),('tablet','tablet')])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MY Products'
        


