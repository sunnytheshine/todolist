import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo
from .serializers import TodoSerializer


# initialize the APIClient app
client = Client()


class GetAllTodolistsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Todo.objects.create(
            title='something')
        Todo.objects.create(
            title='do this')
        Todo.objects.create(
            title='doing')
        Todo.objects.create(
            title='some')

    def test_get_all_todos(self):
        # get API response
        response = client.get(reverse('ListTodo'))
        # get data from db
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateSingleTodoTest(TestCase):
    """ Test module for GET single todo API """

    def setUp(self):
        self.valid_payload = {
            'title': 'Muffin',
        }

        self.invalid_payload = {
            'title': '',
        }

    def test_create_valid_single_todo(self):
        response = client.post(
            reverse('ListTodo'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_todo(self):
        response = client.post(
            reverse('ListTodo'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateTodoTest(TestCase):
    """ Test module for updating an existing todo record """

    def setUp(self):
        self.sunny = Todo.objects.create(
            title='Bread', id=3, done=False)
        self.muffin = Todo.objects.create(
            title='Bread and muffin', id=2, done=False)
        self.valid_payload = {
            'title': 'Bread get from walmart',
            'id': 2,
            'done': False,
        }

        self.invalid_payload = {
            'id': 4,
        }

    def test_valid_update_todo(self):
        response = client.put(
            reverse('DetailTodo', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_todo(self):
        response = client.put(
            reverse('DetailTodo', kwargs={'pk': self.sunny.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class MarkDoneTodoTest(TestCase):
    """ Test module for updating an existing todo record """

    def setUp(self):
        self.sunny = Todo.objects.create(
            title='Bread', id=3, done=False)
        self.muffin = Todo.objects.create(
            title='Bread and muffin', id=2, done=False)
        self.valid_payload = {
            'id': 2,
            'done': True,
        }

        self.invalid_payload = {
        }

    def test_valid_update_todo(self):
        response = client.patch(
            reverse('DetailTodo', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_todo(self):
        response = client.patch(
            reverse('DetailTodo', kwargs={'pk': self.sunny.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTodoTest(TestCase):
    """ Test module for deleting an existing todo record """

    def setUp(self):
        self.sunny = Todo.objects.create(
            title='lets do something', id=1)
        self.veer = Todo.objects.create(
            title='lets do something new', id=2)

    def test_valid_delete(self):
        response = client.delete(
            reverse('DetailTodo', kwargs={'pk': self.sunny.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse('DetailTodo', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)