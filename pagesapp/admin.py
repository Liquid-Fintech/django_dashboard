from django.contrib import admin
from .models import TicketModel, ResponseModel


@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'created_at']
    search_fields = ['user', 'subject']
    list_filter = ['created_at']
    readonly_fields = ['user', 'subject', 'description', 'created_at']


@admin.register(ResponseModel)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    search_fields = ['user']
    list_filter = ['created_at']
    readonly_fields = ['user', 'created_at', 'question1', 'question2', 'question3', 'question4', 'question5']
