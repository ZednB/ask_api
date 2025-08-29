from rest_framework import generics
from questions.models import Question
from questions.serializers import QuestionSerializer, QuestionRetrieveSerializer


class QuestionListApiView(generics.ListAPIView):
    """
    Контроллер для просмотра списка вопросов
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateApiView(generics.CreateAPIView):
    """
    Контроллер для создания вопроса
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveApiView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра конкретного вопроса
    """
    queryset = Question.objects.all()
    serializer_class = QuestionRetrieveSerializer


class QuestionDestroyApiView(generics.DestroyAPIView):
    """
    Контроллер для удаления вопроса
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
