from django.contrib import admin
from . import models

# Register your models here.
class Product_pictureAdmin(admin.ModelAdmin):
    list_display = ['pk', 'picture_name', 'picture_icron', 'picture_datetime','picture_isDelete' ,'picture_foreKey','icon_img']
    readonly_fields = ['icon_img']
admin.site.register(models.Product_picture,Product_pictureAdmin)