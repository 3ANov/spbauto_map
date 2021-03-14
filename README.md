# spbauto_map
Проект в рамках ДоброHack'a для замены карты с дорожными проблемами СпБ и ЛенОбласти  
**Работающий прототип на heroku**: https://spbauto.herokuapp.com/ *(возможна задержка доступа - особенность платформы)*  

Проект разрабатывается с использованием docker-compose.
Для развертывания необходимо:  
- скачать проект:
    - **git clone** _https://github.com/3ANov/spbauto_map_
- создать файлы **.env.dev** или **.env.prod** в директории **env**  
  по образцу **.env.example** в соответствии с требованиями для тестового  
  прототипа проекта, или для финальной, "релизной" версии;
- собрать образ проекта в docker'e:
    - **docker-compose build**
- применение миграций:
    - **docker-compose exec web python manage.py migrate**
- запуск тестов:
    - **docker-compose exec web python manage.py test**
- запустить проект:
    - **docker-compose up -d**
- для остановки контейнеров:
    - **docker-compose down**
