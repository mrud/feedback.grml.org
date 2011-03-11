from django.contrib.syndication.views import Feed
from feedback.models import Feedback

class FeedbackFeed(Feed):
    title = "Grml Feedback feed"
    link = "/sitenews/"
    description = "Feed with all submiteed feedbacks."

    def items(self):
        return Feedback.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        begin = 'A'
        if not item.is_happy():
            begin = 'An'
        return "%s %s user wrote about Grml %s" % (begin, item.get_kind_display(),
                item.version)

    def item_description(self, item):
        return item.text

    def item_pubdate(self, item):
        return item.pub_date


