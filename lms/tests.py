from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='TestUser@test.com', password='qwer123qwer', first_name='Test',)
        self.course = Course.objects.create(title='Test Course', description='Test Course description',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson',
                                            description='Test Lesson description',
                                            link_to_video='https://www.youtube.com/wood/',
                                            lesson_course=self.course,
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        url = reverse('lms:course-list')
        data = {
            'title': 'Test Course',
            'description': 'Test Course description',
            'preview': '',
            'owner': self.user.pk,


        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_retrieve(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        result = {
            'id': self.course.pk,
            'title': 'Test Course',
            'description': 'Test Course description',
            'preview': None,
            'count_lesson': 1,
            'lessons': [
                       {
                           'id': self.lesson.id,
                           'title': 'Test Lesson',
                           'description': 'Test Lesson description',
                           'preview': None,
                           'link_to_video': 'https://www.youtube.com/wood/',
                           'lesson_course': self.course.pk,
                           'owner': self.user.id
                       }
                       ],
            'owner': self.user.pk,
            'subscription_course': False}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_course_update(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        data = {
            'title': 'Test Course 2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Test Course 2'
        )

    def test_course_delete(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse('lms:course-list')
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                            {
                                'id': self.course.pk,
                                'title': 'Test Course',
                                'description': 'Test Course description',
                                'preview': None,
                                'count_lesson': 1,
                                'lessons': [
                                           {
                                               'id': self.lesson.id,
                                               'title': 'Test Lesson',
                                               'description': 'Test Lesson description',
                                               'preview': None,
                                               'link_to_video': 'https://www.youtube.com/wood/',
                                               'lesson_course': self.course.pk,
                                               'owner': self.user.id
                                           }
                                           ],
                                'owner': self.user.pk,
                                'subscription_course': False
                            }
                        ]
                 }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='TestUser@test.com', password='qwer123qwer', first_name='Test')
        self.course = Course.objects.create(title='Test', description='Test description')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        url = reverse('lms:subscription-create')
        data = {'user_subscription': self.user.pk,
                'user_course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка добавлена'})

    def test_subscription_deactivate(self):
        url = reverse('lms:subscription-create')
        Subscription.objects.create(user_subscription=self.user, user_course=self.course)
        data = {'user_subscription': self.user.pk,
                'user_course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка удалена'})
