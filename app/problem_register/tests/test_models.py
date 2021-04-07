from django.contrib.gis.geos import Point
from django.test import TestCase
from django.utils import timezone

from problem_register.models import ProblemLabel, Status


class NewProblemReportTest(TestCase):
    """тест добавления проблемы"""

    def setUp(self):
        """добавление в базу"""
        ProblemLabel.objects.create(id=1,
                                    created_date=timezone.now(),
                                    geom=Point((30.333144, 59.931327)),
                                    description='Новая тестовая проблема на дороге')

    def test_problem_report_creation(self):
        """тест: создание репорта на проблему"""
        problem = ProblemLabel.objects.get(id=1)
        self.assertEqual(problem.description, 'Новая тестовая проблема на дороге')

    def test_problem_report_coordinate(self):
        """тест: проверка координат проблемы"""
        problem = ProblemLabel.objects.get(id=1)
        self.assertEqual(problem.geom.x, 30.333144)
        self.assertEqual(problem.geom.y, 59.931327)


class NewStatusReportTest(TestCase):
    """тест добавления статуса проблемы"""

    def setUp(self):
        """добавление в базу"""
        Status.objects.create(name='Новый статус')

    def test_get_status(self):
        """тест: существует ли статус с таким именем"""
        status_set = Status.objects.filter(name='Новый статус')
        self.assertEqual(status_set.count(), 1)
