from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        return f'Title: {self.title} -> Created at: {self.created_at}'

    def __repr__(self):
        return self.__str__()
