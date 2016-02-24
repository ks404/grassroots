from django.contrib import admin
from .models import FedCongressPerson

# Register your models here.
@admin.register(FedCongressPerson)
class FedCongressPersonAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    list_filter = ('in_office', 'chamber',)


