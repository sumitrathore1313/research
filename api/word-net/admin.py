from django.contrib import admin
from .models import WordNet

# Register your models here.
@admin.register(WordNet)
class WordNetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
    search_fields = ('name',)