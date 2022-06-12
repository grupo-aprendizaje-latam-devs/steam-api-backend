# Proyecto del grupo de aprendizaje 1 (Steam API)

🌱 Éste proyecto apenas está en comienzo. El tema: Sitio web para implementar un API que muestra datos sobre juegos de Steam

Meta y propósitos:

- Aprender a utilizar tecnologías de programación en un ambiente full-stack
- Aprender a crear aplicaciones con Python y el framework web Django
- Aprender a manejar bases de dato con PostgreSQL

Ésta será la única sección del proyecto que estará en inglés. Ésto es hecho a propósito, y busca ayudar a mejorar el nivel de inglés profesional, además de que la programación y mayoría de fuentes existen todas en inglés.

**¡Ánimo!**

# Table of Contents

1. [Specs](#spec)
1. [Useful commands](#useful-commands)
2. [Setup](#setup)

**Note**: it's recommended to read the [Django tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) if you're not familiar with the Django framework.

## Specs

- Web framework: Django
- Database: SQLite 3
- API: [cheapshark.com](https://apidocs.cheapshark.com/)

The project `steam_api` handles all commands while `games` is the app that contains all business logic that interacts with the Steam API.

Here's a picture of the high-level architecture diagramme:

![Architecture diagramme](https://i.ibb.co/DR68Dj8/Screen-Shot-2022-06-13-at-11-05-50-AM.png)

## Useful commands

- Start the server: `python manage.py runserver`
  - On a custom port: `python manage.py runserver <X>` (`<X>` being the port number i.e. `8080`)
- Migrate the database: `python manage.py migrate`
- Update database models: `python manage.py makemigrations <X>` (`<X>` being the name of the app i.e. `games`)

## Setup

### Requirements

- [Python 3.8.x](https://www.python.org/downloads/)
- [PostgreSQL 13.4](https://www.postgresql.org/download/)

#### Installation

1) Create a virtual environment to handle project dependencies

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Create/migrate the database

```shell
python manage.py migrate
```

3) Run the server

```shell
python manage.py runserver
```

4) Visit your live server: `http://127.0.0.1:8000/games`