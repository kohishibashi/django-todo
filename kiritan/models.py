from django.db import models


class Task(models.Model):
    title = models.CharField('タイトル', max_length=200)
    complete = models.BooleanField('完了', default=False)
    updated_at = models.DateTimeField('更新', auto_now=True)
    creted_at = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.title
