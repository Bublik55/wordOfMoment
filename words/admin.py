from csv import list_dialects
from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
  list_display = ('owner_id', 'content', 'count')


admin.site.register(Word)
