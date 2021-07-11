import datetime
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


class Post(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField()
    public = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True, null=True)
    slug = models.SlugField(default="",editable=False,max_length=150, blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    
    def save(self,*args, **kwargs):
                
        if not self.slug:
            now = datetime.datetime.now()
            total_time = datetime.timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s-%s' % (self.title, str(seconds))
            self.slug = slugify(slug_unique)
            
        super(Post,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title