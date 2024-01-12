from django.db import models

# Create your models here.

class Book_category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=100)
    book_type = models.ForeignKey(Book_category, on_delete=models.CASCADE,null=True)
    discription = models.TextField()
    image = models.FileField(upload_to='', blank = True, null = True)
    borrowing_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    

