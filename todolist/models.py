from datetime import timezone, datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(default=datetime.now())

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
