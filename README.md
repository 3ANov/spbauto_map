# spbauto_map
Проект в рамках ДоброHack'a для замены карты с дорожными проблемами СпБ и ЛенОбласти  
**Работающий прототип на heroku**: https://spbauto.herokuapp.com/ *(возможна задержка доступа - особенность платформы)*  
**Требования**: см requirements.txt

Используется postgresql-12 и postgis  
Имя базы данных: geomap_db  
Имя пользователя базы: testuser  
Пароль: testuser  

После создания базы в postgres, необходимо для неё добавить(создать) расширение postgis.  
(можно выполнить запрос к базе CREATE EXTENSION postgis;)

Для применения миграций необходимо в _**map/urls.py**_ закоментировать  **path('accounts/', include('accounts.urls'))**  

В проекте используется обратное геокодирование с помощью геокодера **jrg** (_https://github.com/gojuno/jrg_)  
Для запуска контейнера использовать: **docker run --rm --name geocoder -v pgdata:/pgdata -d -p 8080:80 jrg**  
