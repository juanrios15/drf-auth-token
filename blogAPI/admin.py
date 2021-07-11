from django.contrib import admin
from .models import Post, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title','summary', 'public', 'created_at')
    readonly_fields = ('slug', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)