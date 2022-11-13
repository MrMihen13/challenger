# Challenger


- [Technical requirements for developers](#technical-requirements-for-developers)
- [Local run](#local-run)
    - [Local run without](#local-run-without-docker-compose)
    - [Local run with docker-compose](#local-run-with-docker-compose)
- [Project documentations](#project-documentation)
- [Environments and dependencies](#environments-and-dependencies)

-------------------------------------------------------------------------

## Get started

### Локальный запуск

Для того чтобы начать работу на локальном устройстве, необходимо локально запустить сервер. Чтобы его запустить
необходимо выполнить несколько простых шагов.

1. Создать файл `.env`, скопировать в него переменные из файла `.emv.template` и задать переменные окружения. 
   Если вы не хотите использовать Sentry для отслеживания ошибок, нужно в настройках удалить следующий блок кода:

    ```python
    sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True
    )
    ```

    В противном случае сервер не удастся запустить, если не задать в файле `.env` переменную `SENTRY_DSN`

2. Создать [виртуальное окружение](#environments)
3. Запустить docker контейнер с базой данных 

    ```commandline
    docker-compose build
    ```
4. Применить все необходимые миграции командой `>> python manage.py migrate`. Эта команда создает таблицы в базе данных.
5. Запустить сервер с помощью команды `>> python manage.py runserver`

Если вы все сделали правильно, то в консоли вы увидите следующий вывод:

```
System check identified no issues (0 silenced).
April 17, 2022 - 18:46:34
Django version 4.0.4, using settings 'chellenger.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

-------------------------------------------------------------------------

## Environments and dependencies

### Environments

В проекте используется [Poetry](https://python-poetry.org/) для работы с проектом с помощью виртуального окружения. 
Если не установлена на вашем устройстве, то необходимо [установить](https://python-poetry.org/docs/#installing-with-pipx)

Следующая команда создает виртуальное окружение на вашем устройстве. Для корректной работы необходимо наличие Python 
версии 3.10. Если у вас не установлен Python, инструкция по установке доступна [здесь](https://www.python.org/downloads/release/python-3108/).

```commandline
 pipenv shell
```

Для установки всех зависимостей проекта в виртуально окружении, нужно воспользоваться следующей командой.

 ``` commandline
 pipenv install
 ```

Эта команда устанавливает все зависимости из файла с зависимостями [проекта](#dependencies).


### Dependencies

Информация о всех зависимостях проекта можно найти в файле [pyproject.toml](./pyproject.toml)

-------------------------------------------------------------------------

## Project documentation

Project documentations is avaliable [here](./docs/project_documentations.md)

-------------------------------------------------------------------------