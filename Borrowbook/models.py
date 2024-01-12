from django.db import models
from django.contrib.auth.models import User
from Book.models import Books

# Create your models here.
ratting = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

class Borrowedbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrowing_date = models.DateField(auto_now_add=True)
    returning_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rating = models.CharField( max_length=50, choices=ratting)
    comment = models.TextField()

    def __str__(self):
        return self.rating