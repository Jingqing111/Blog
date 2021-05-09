from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

# 为了文章列表显示更加详细的信息
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # list—display属性控制post列表页展示的字段

    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    # 此外还有一个 fields 属性，则用来控制表单展现的字段

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)