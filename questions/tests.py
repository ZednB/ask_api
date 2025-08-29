import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from questions.models import Question


@pytest.mark.django_db
def test_create_question():
    """
    Тест на успешное создание вопроса
    """
    client = APIClient()
    data = {'text': 'Тестовый вопрос создался?'}
    url = reverse('questions:question_create')
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert Question.objects.count() == 1
    assert Question.objects.first().text == 'Тестовый вопрос создался?'


@pytest.mark.django_db
def test_get_questions_with_answers():
    """
    Тест на наличие ответов в каждом вопросе
    """
    client = APIClient()
    q = Question.objects.create(text='Снова тестовый вопрос')
    url = reverse('questions:question_retrieve', args=[q.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == q.id
    assert response.data['text'] == 'Снова тестовый вопрос'
    assert response.data['answers'] == []
