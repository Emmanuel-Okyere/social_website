"""Models for images app"""
from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.
class Image(models.Model):
    """Image Model class"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    related_name="images_created", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to = "images/%Y/%m/%d/")
    description = models.TextField(max_length=200, blank=True)
    created = models.DateField(db_index=True, auto_now_add=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
    related_name="image_liked", blank = True)

    def __str__(self):
        """Returning human readable string"""
        return self.title

    def save(self, *args, **kwargs):
        """Overiding the save method"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
