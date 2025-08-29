from django.urls import path

from questions.apps import QuestionsConfig
from questions.views import QuestionListApiView, QuestionCreateApiView, QuestionRetrieveApiView, QuestionDestroyApiView

app_name = QuestionsConfig.name

urlpatterns = [
    path('', QuestionListApiView.as_view(), name='question_list'),
    path('create/', QuestionCreateApiView.as_view(), name='question_create'),
    path('retrieve/<int:pk>/', QuestionRetrieveApiView.as_view(), name='question_retrieve'),
    path('destroy/<int:pk>/', QuestionDestroyApiView.as_view(), name='question_destroy'),
]
