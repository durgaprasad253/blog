from django.contrib import admin
from . models import Author,Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","tag","date")
    list_display=("title","author","date")
admin.site.register([Author,Tag])
admin.site.register(Post,PostAdmin)


