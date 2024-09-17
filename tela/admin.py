from django.contrib import admin
from tela.models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'date', 'problem')
    search_fields = ('meeting', 'date')


admin.site.register(Meeting, MeetingAdmin)
