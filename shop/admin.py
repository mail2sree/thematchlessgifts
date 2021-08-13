from django.contrib import admin
from django.db.models.query import QuerySet
from .models import*

# Register your models here.
admin.site.site_header = 'Matchless Gifts'
admin.site.site_title = 'Matchless Gifts | Admin Page'
admin.site.index_title = "Manage Matchless Gifts Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request):
        QuerySet.update(category="Book")
    
    list_display = ('title','price', 'disount_price', 'category', 'description','image')
    search_fields = ('title','price', 'disount_price', 'category', 'description','image')
    actions = ('change_category_to_default')
    list_editable = ('price', 'disount_price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'username', 'email', 'address', 'address2', 'country', 'city', 'state', 'zip', 'orderstatus', 'total')
    search_fields = ('firstname', 'lastname', 'username', 'email', 'address', 'address2', 'country', 'city', 'state', 'zip', 'orderstatus', 'total')
    list_editable = ('orderstatus', 'email')
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)