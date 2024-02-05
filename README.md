Приложение для рассылки сообщений.
Для начала работы вам нужно слонировать приложение на свой компьютер.
```
git clone https://github.com/IgorSorokin1985/CW6_mailing_of_letters.git
```
Установить все зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Создать базу данных.
```
CREATE DATABASE mailing_database
```
Настроить подключение в своей базе данных.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database',
        'USER': 'postgres',
        'PORT': '5433',
        'PASSWORD': '123qwe',
    }
}
```
Создать миграции.
```
python manage.py makemigrations
```
Установить мирграции
```
python manage.py migrate
```
Создать файл .env и ввести в него свои данные.
```
EMAIL_HOST=
EMAIL=
EMAIL_PASSWORD=
CACHE_ENABLED=
CACHE_LOCATION=
```

Для создания супер пользователя воспользуйтесь командой
```
python manage.py csu
```

Для запуска автоматической отправки рассылок вам следует использовать команду
```
python manage.py runapscheduler
```

Для разовой отправки всех готовых рассылок вам следует использовать команду
```
python manage.py runmailings
```