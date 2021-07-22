from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'body']
    class Meta:
        model = Article


admin.site.register(Article, ArticleModelAdmin)