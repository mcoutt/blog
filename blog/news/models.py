from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"
