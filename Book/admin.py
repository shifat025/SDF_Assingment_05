from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Books) 



class Book_category_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=['name','slug']

admin.site.register(models.Book_category,Book_category_Admin) 