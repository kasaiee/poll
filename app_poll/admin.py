from django.contrib import admin
from app_poll.models import Poll

class PollAdmin(admin.ModelAdmin):
    search_fields = ('__all__', )
    list_filter = ('vaziat_isargari', )

admin.site.register(Poll, PollAdmin)
