from django.db.models import signals
from django.dispatch import receiver

from .models import Member, Membership

@receiver(signals.post_save, sender=Member)
def membership(sender, instance, **kwargs):
    mp = Membership.objects.get_or_create(ok=True)
    mp[0].members.add(instance)