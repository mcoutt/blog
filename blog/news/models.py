from django.db import models
from django.template.defaultfilters import slugify
from time import time


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        str_time = "".join(str(time()).split("."))
        string = "%s-%s" % (str_time[7:], self.title)
        self.slug = slugify(string)
        super(News, self).save()
