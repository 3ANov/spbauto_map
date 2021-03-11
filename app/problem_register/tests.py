from django.contrib.gis.geos import Point
from django.test import TestCase
from django.utils import timezone

from problem_register.models import ProblemLabel


class NewProblemReportTest(TestCase):
    """тест добавления проблемы"""

    def setUp(self):
        """добавление в базу"""
        ProblemLabel.objects.create(created_date=timezone.now(),
                                    geom=Point((30.333144, 59.931327)),
                                    description='Новая тестовая проблема на дороге')

    def test_get_problem_report(self):
        """тест: сравнение добавленной на карту точки"""
        problem = ProblemLabel.objects.get(description='Новая тестовая проблема на дороге')
        self.assertEqual(problem.geom.x, 30.333144)
        self.assertEqual(problem.geom.y, 59.931327)
