from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


from rest_framework.authtoken.models import Token
from django.template.defaultfilters import slugify

# Create your models here.


class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    slug = models.SlugField(default="",editable=False,max_length=150, blank=True, null=True)
    
    def save(self,*args, **kwargs):
        
        if not self.slug:
            
            self.slug = slugify(self.username)

        super(User,self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)