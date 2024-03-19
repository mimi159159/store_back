from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    cat = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    fields =['desc','price', 'cat']
 
    def __str__(self):
           return self.desc
    
class categories(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    cat = models.ForeignKey(Product,null=True,blank=True, on_delete=models.CASCADE )
    fields =['desc','cat']
 
    def __str__(self):
           return self.desc
    

class orders(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE )
    date =models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=5,decimal_places=2)
    fields =['user','date','total']
 
    def __str__(self):
           return self.date


class orderDetail(models.Model):
    order = models.ForeignKey(orders,null=True,blank=True, on_delete=models.CASCADE )
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE )
    total = models.DecimalField(max_digits=5,decimal_places=2)
    fields =['order','user','total']
 
    def __str__(self):
           return self.total



class profile(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE )
    age = models.DecimalField(max_digits=5,decimal_places=2)
    city = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True, default='person')
    fields =['user','age','city','gender']
 
    def __str__(self):
           return self.age


