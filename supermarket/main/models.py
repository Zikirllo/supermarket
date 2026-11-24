from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=55)
    price=models.FloatField(default=0)
    text=models.TextField(max_length=500)
    image=models.ImageField(upload_to="")
    datetime=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name