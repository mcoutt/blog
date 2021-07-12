from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "content",
        "created_date",
        "modified_date"
    ]

    readonly_fields = ["created_date", "modified_date"]
