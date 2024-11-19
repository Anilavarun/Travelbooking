from django.db import models
from django.template.defaultfilters import slugify
from services.models import*
from django.urls import reverse


# Create your models here.


class hotels(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('list_cat',args=[self.slug])

class list(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)
    place= models.CharField(max_length=100)
    check_date = models.DateField(null=True)
    check_time = models.TimeField()
    img = models.CharField(max_length=9999)
    single = models.CharField(max_length=9999,null=True)
    deluxe = models.CharField(max_length=9999,null=True)
    executive = models.CharField(max_length=9999,null=True)
    one = models.TextField(max_length=99,null=True)
    two = models.TextField(max_length=99,null=True)
    three = models.TextField(max_length=99,null=True)
    first = models.CharField(max_length=999,null=True)
    second = models.CharField(max_length=999,null=True)
    third = models.CharField(max_length=999,null=True)
    fourth = models.CharField(max_length=999,null=True)
    fifth = models.CharField(max_length=999,null=True)
    sixth = models.CharField(max_length=999,null=True)
    firstprice = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    secondprice = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    thirdprice = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    firstdesc= models.TextField(max_length=99,null=True)
    seconddesc= models.TextField(max_length=99,null=True)
    thirddesc= models.TextField(max_length=99,null=True)
    category = models.ForeignKey(hotels,on_delete=models.CASCADE,null=True)

    def __str__(self):
         return self.name
    
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
