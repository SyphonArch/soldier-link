from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(default=timezone.now)
    sent = models.BooleanField(default=False)
    send_attempt_over = models.BooleanField(default=False)

    def __str__(self):
        fail_str = '[FAIL] ' if not self.sent else ''
        return fail_str + self.get_header()

    def get_header(self):
        return self.sender + ': ' + self.subject

    @classmethod
    def create(cls, sender, subject, content):
        return cls(sender=sender, subject=subject, content=content)
