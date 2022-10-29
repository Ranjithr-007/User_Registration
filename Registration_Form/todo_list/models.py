from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254)
    Mobile = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    def __str__(self):
        return self.Name




