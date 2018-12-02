## Python Prefork HTTP server
### Задание:
Разработать веб-сервер для отдачи статики с диска. Язык программирования и технологию многопоточной обработки соединений выбрать самостоятельно. Разрешается использовать библиотеки помогающие реализовать асинхронную обработку соединений (libevent/libev и им подобные), запрещается использовать библиотеки реализующие мультипоточную обработку или какую-либо часть обработки HTTP.
Провести нагрузочное тестирование, проверку стабильности и корректности работы.

Требования и методика тестирования по ссылке: https://github.com/init/http-test-suite

### Запуск:
Для запуска сервера есть 2 способа:
1. ``` python3 ./server.py ```
   В этом случае данные конфигурации сервера будут браться из файла ```httpd.conf```, который должен находиться по пути: ```/etc/httpd.conf```. Пример такого файла находится в репозитории.
2. ``` python3 ./launch.py --ncpu=NCPU --root=ROOT ```
   В этом случае количество процессов и root - директория статики можно определить аргументами при запуске сервера. Если аргументы не заданы, то данные конфигурации будут браться из файла ```/etc/httpd.conf```.
   
### Запуск docker контейнера с сервером:
1. ```sudo docker build -t server-httpd https://github.com/InfantryMan/webserver.git``` - создание образа.
2. ```sudo docker run -p 8000:80 -v /var/www/html:/var/www/html:ro --name server-httpd -t server-httpd``` - запуск контейнера. Проброс 8000 порта хоста на 80 порт контейнера.
  
##### Путь к файлу ```httpd.conf``` можно поменять в файле launch.py
##### Сервер показывает такой же порядок RPS, как nginx.

## Have fun!