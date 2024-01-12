from django.db import models
from django.contrib.auth.models import User
from Book.models import Books
# Create your models here.

class account(models.Model):
    user = models.OneToOneField(User,related_name='account',unique=True, on_delete=models.CASCADE)
    diposit = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank = True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   

    def __str__(self):
        return self.user.username
    
    