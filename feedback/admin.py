
from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'kind', 'text', 'version']
    fields = ('kind', 'text', 'version', 'ip_address')
    readonly_fields = ('ip_address', )
    list_filter = ('pub_date', 'kind', 'version')
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        obj.ip_address = request.META['REMOTE_ADDR']
        obj.save()



admin.site.register(Feedback, FeedbackAdmin)
