from django.contrib import admin
from .models import Tag , Author, Posts, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","author","pub_date")
    list_filter = ("pub_date","tagline","author",)
    

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Posts,PostAdmin)


