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
        return "{0} {1} user wrote about Grml {2.version}".format(begin, item.get_kind_display(), item)

    def item_description(self, item):
        return item.text

