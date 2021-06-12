from .models import Message
from datetime import date


def check(limit=30):
    rslt = Message.objects.filter(timestamp__date=date.today())
    if len(rslt) < limit:
        return True
    else:
        return False
