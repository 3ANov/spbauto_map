from django.contrib.gis.geos import Point
from django.test import TestCase
from django.utils import timezone

from problem_register.forms import ProblemLabelForm
from problem_register.models import ProblemLabel


class NewProblemReportTest(TestCase):
    def setUp(self):
        """добавление в базу"""
        ProblemLabel.objects.create(id=1,
                                    created_date=timezone.now(),
                                    geom=Point((30.333144, 59.931327)),
                                    description='Новая тестовая проблема на дороге')

    def test_valid_form(self):
        """тест: проверка формы с валидными данными"""
        problem = ProblemLabel.objects.get(id=1)
        data = {'description': problem.description, 'geom': problem.geom}
        form = ProblemLabelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """тест: проверка формы с невалидными данными"""
        problem = ProblemLabel.objects.get(id=1)
        data = {'description': '', 'geom': problem.geom}
        form = ProblemLabelForm(data=data)
        self.assertFalse(form.is_valid())
