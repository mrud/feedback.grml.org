from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from feedback.models import Feedback
from feedback.feeds import FeedbackFeed

info_dict = {
    'queryset': Feedback.objects.all(),
}


urlpatterns = patterns('feedback.views',
    url(r'^$', 'index', name='feedback_index'),
    url(r'^(?P<filter_by>\w+)/(?P<page>\d+)?/$', 'show_list', name='show_list'),
)
urlpatterns += patterns('',
    url(r'show/(?P<object_id>\d+)$',
    'django.views.generic.list_detail.object_detail', info_dict, name='show_message'),
    url(r'^rss$', FeedbackFeed(), name="feedback_rss"),
 )
