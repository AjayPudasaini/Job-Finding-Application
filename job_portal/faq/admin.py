from django.contrib import admin
from faq.models import Faqs

@admin.register(Faqs)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_on', 'for_who']
