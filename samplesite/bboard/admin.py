from django.contrib import admin

from .models import Goods
from .models import Rubric

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'category')
    search_fields = ('title', 'category', 'rubric')

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Rubric)