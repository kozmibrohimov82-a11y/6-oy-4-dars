from django.db import models

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=125)
    description=models.CharField(blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=0)
    description=models.TextField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=False)

    def __str__(self):
        return self.name



