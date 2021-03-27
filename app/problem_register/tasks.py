import logging
from datetime import datetime

from main.celery import app

logger = logging.getLogger(__name__)


@app.task()
def add_places_task(pk):
    logger.info('Добавление данных для проблемы %s время: %s', str(pk), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return True