import uuid

from django.db import models

from questions.models import Question


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers',
                                    verbose_name='Идентификатор вопроса')
    user_id = models.UUIDField(default=uuid.uuid4, verbose_name='Идентификатор пользователя')
    text = models.TextField(verbose_name='Текст ответа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ответа')

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
