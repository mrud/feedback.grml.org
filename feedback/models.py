from django.db import models

FEEDBACK_CHOICE = (
    ('h', 'happy'),
    ('u', 'unhappy'),
)

class Feedback(models.Model):
    """
    Class representing feedback from users
    """
    kind = models.CharField(max_length=1, choices=FEEDBACK_CHOICE)
    version = models.CharField(max_length=75, blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()

    def is_happy(self):
        return self.kind == 'h'

    @models.permalink
    def get_absolute_url(self):
        return ('show_message', [str(self.id)])


