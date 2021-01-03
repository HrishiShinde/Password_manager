from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    userEmail = models.CharField(max_length=50,  default = 'NaN')
    userPass = models.CharField(max_length=15)
    class Meta:
        db_table = "User"
        
class Password(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    siteName = models.CharField(max_length=50)
    sitePass = models.CharField(max_length=15)
    class Meta:
        db_table = "Password"