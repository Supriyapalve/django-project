from django.db import models




class ipo_models(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    DOB = models.DateField()
    profession = models.CharField(max_length=25)
    contact_no = models.BigIntegerField()
    ipoamount = models.IntegerField()

# Create your models here.
