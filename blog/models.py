from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title
