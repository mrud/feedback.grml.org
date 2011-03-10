
from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'kind', 'text', 'version']
    fields = ('kind', 'text', 'version', 'ip_address')
    readonly_fields = ('ip_address', )
    list_filter = ('pub_date', 'kind', 'version')
    date_hierarchy = 'pub_date'


admin.site.register(Feedback, FeedbackAdmin)
