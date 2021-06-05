import logging
from datetime import datetime

from main.celery import app
from problem_register.services import add_places_info_for_problem

logger = logging.getLogger(__name__)


@app.task(ignore_result=True, rate_limit='1/s')
def add_places_task(pk):
    """ Celery-задача для добавления геотегов (название улицы, города и т.д.) в модель дорожной проблемы """
    logger.info('Добавление данных для проблемы %s время: %s', str(pk), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    add_places_info_for_problem(pk)

