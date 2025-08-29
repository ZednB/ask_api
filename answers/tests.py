import uuid

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from answers.models import Answer
from questions.models import Question


@pytest.mark.django_db
def test_create_answer():
    """
    Тест на создание ответа на вопрос
    """
    client = APIClient()
    q = Question.objects.create(text='Тестовый вопрос для нашего ответа')
    data = {
        "question_id": q.id,
        "user_id": str(uuid.uuid4()),
        "text": "Вот и наш ответ"
    }
    url = reverse('answers:create_answer')
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert Answer.objects.count() == 1
    answer = Answer.objects.first()
    assert answer.text == 'Вот и наш ответ'
    assert answer.question_id_id == q.id


@pytest.mark.django_db
def test_get_answer():
    """
    Тест на получение ответа
    """
    client = APIClient()
    q = Question.objects.create(text='Вопрос')
    a = Answer.objects.create(
        question_id=q,
        user_id=uuid.uuid4(),
        text='Ответ'
    )
    url = reverse('answers:retrieve_answer', args=[q.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == a.id
    assert response.data['text'] == 'Ответ'


@pytest.mark.django_db
def test_answer_to_none_question():
    """
    Создадим ответ к несуществующему вопросу
    """
    client = APIClient()
    data = {
        'question_id': 1,
        'user_id':uuid.uuid4(),
        'text':'Ответ'
    }
    url = reverse('answers:create_answer')
    response = client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'question_id' in response.data
