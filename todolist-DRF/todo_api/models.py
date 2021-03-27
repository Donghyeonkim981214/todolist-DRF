from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Todo(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  string_id = models.CharField(max_length=2, null=True, blank=True)
  order_num = models.IntegerField(null=True, blank=True)
      
  def __str__(self):
    return self.title

@receiver(post_save, sender=Todo)
def order_listing_update(sender, instance, created, **kwargs):
    if created:
        instance.order_num = instance.id
        instance.string_id = str(instance.id)
        instance.save()