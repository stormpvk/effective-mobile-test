<div align=center><img width="410" height="274" alt="image" src="https://github.com/user-attachments/assets/3d06ef76-f4e3-4aed-b4a0-4cfafd5bd93b" /></div>
<div align=center><h1>Реализация тестового задания на позицию DevOps</h1></div>
<div align=center><h2>Исполнитель Корнев А.А.</h2></div>
Проект разворачивает два контейнера с приложениями (nginx и python http.sever) с помощью файла docker-compose.yml, после чего контейнеры взаимодействуют друг с другом.</br>
<h3>1. Установка</h3>
Предварительные требования: на хосте должны быть установлены пакеты docker, docker compose, git.</br>
Предполагается, что все действия выполняются с правами пользователя <b>root</b>.<br>
Необходимо создать папку для клонирования проекта из git репозитория, в примере использутся папка <b>projects</b>:</br>
<code>mkdir /projects</code></br>
После создания папки необходимо перейти в нее:</br>
<code>cd /projects</code></br>
На следующем этапе необходимо клонировать репозиторий и перейти в папку клонированного репозитория:</br>
<code>git clone https://github.com/stormpvk/effective-mobile-test.git && cd effective-mobile-test</code></br>
Далее выполняется развертывание котейнеров с приложениями командой:</br>
<code>docker compose up --build -d</code></br>
Развернутые контейнеры будут запущены. Установка завершена.</br>
<h3>2. Проверка работы</h3>
Проверить работу контейнеров можно командой:</br>
<code>docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.ID}}"</code></br>
При успешно работающих контейнерах вывод должен быть следующим:</br>
<img width="1066" height="74" alt="image" src="https://github.com/user-attachments/assets/6cc79bf7-d479-4c0b-9dc7-787b5aac654f" />
Видно что контейнеры запущены и здоровы.</br>
Следующим этапом необходимо проверить работу приложений. Это можно сделать следующим образом:</br>
а. С docker хоста выполнить команду <code>curl http://localhost</code>, команда должна вернуть ответ <code>Hello from Effective Mobile!</code></br>
б. Из контейнера nginx выполнить ту же команду <code>curl http://localhost</code>, ответ так же будет <code>Hello from Effective Mobile!</code></br>
в. Из контейнера nginx выполнить команду <code>curl http://backend:8080</code>, ответ <code>Hello from Effective Mobile!</code></br>
<h3>3. Схема работы приложений</h3>
При запуске котейнера nginx в нем запускается web сервер nginx с проброшенным 80 портом на 80 порт хоста, настроенный в качестве Reverse proxy, 
который проксирует входящие запросы на 80 порт на порт 8080 контейнера backend.</br>
При запуске контейнера backend в нем запускается приложение python3 http.server с EXPOSE портом 8080. При входящем запросе на этот порт сервер отдает 
строку <code>Hello from Effective Mobile!</code>.</br>
Общая схема работы:</br>
- хост получает http запрос на 80 порт и перенаправляет его на 80 порт контейнера nginx</br>
- nginx, получив запрос на 80 порт, перенаправляет его через Reverse proxy на порт 8080 контейнеру backed</br>
- контейнер backend с запущенным http.server получает запрос на 8080 порт и отдает строку <code>Hello from Effective Mobile!</code></br>
