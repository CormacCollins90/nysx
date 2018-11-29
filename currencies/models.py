from django.db import models

# Create your models here.

class Currency(models.Model):
    flag= models.CharField(max_length=20, null=False, blank=False)
    symbol= models.CharField(max_length=3, null=False, blank=False)
    rate= models.DecimalField(max_digits=6, decimal_places=4 ,null=False, blank=False, default=1)
    name= models.CharField(max_length=3, null=False, blank=False)
    
    
    def __str__(self):
        return self.name