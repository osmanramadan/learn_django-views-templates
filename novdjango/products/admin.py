from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category','active')
    list_display_links = ('category','price')
    list_editable = ('active','name')
    search_fields = ('category','price')
    list_filter = ('category','price','active')




admin.site.register(Product,ProductAdmin)



admin.site.site_header = 'Osman Admin'
admin.site.site_title = 'Osman Admin Panel'
admin.site.index_title = 'Welcome to Osman Admin Panel'



