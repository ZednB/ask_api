from rest_framework import generics
from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerCreateApiView(generics.CreateAPIView):
    """
    Контроллер для создания ответов
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveApiView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра конкретного ответа
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDestroyApiView(generics.DestroyAPIView):
    """
    Контроллер для удаления ответа
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

