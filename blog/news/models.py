from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

