from django.urls import path

from answers.apps import AnswersConfig
from answers.views import AnswerCreateApiView, AnswerRetrieveApiView, AnswerDestroyApiView

app_name = AnswersConfig.name

urlpatterns = [
    path('create/', AnswerCreateApiView.as_view(), name='create_answer'),
    path('retrieve/<int:pk>/', AnswerRetrieveApiView.as_view(), name='retrieve_answer'),
    path('destroy/<int:pk>/', AnswerDestroyApiView.as_view(), name='destroy_answer'),
]
