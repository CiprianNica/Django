from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12,blank=True, null=True)
    movil = models.CharField(max_length=12,blank=False, null=False)
    email = models.EmailField()
    compania = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name