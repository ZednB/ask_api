from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания вопроса')

    def __str__(self):
        return f"{self.text}"

    class Meta:
        veerbose_name = 'Вопрос'
        veerbose_name_plural = 'Вопросы'
