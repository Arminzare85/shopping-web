from django.contrib import admin
from store.models import  Product , Category , Comment , Wishlist
# Register your models here


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','rating')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'comment',
        'created_time'
    )
class WishListAdmin(admin.ModelAdmin):
    list_display=('user','product')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Wishlist,WishListAdmin)
