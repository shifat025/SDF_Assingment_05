from django.contrib import admin
from . import models
# Register your models here.
class account_admin(admin.ModelAdmin):
    list_display=['get_first_name','account_balance']
    def get_first_name(self,obj):
        return obj.user.first_name
admin.site.register(models.account) 