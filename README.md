# Proyecto del grupo de aprendizaje 1 (Steam API)

🌱 Éste proyecto apenas está en comienzo. Todavía no hemos decidido el tema.

Meta y propósitos:

- Aprender a utilizar tecnologías de programación en un ambiente full-stack
- Aprender a crear aplicaciones con Python y el framework web Django
- Aprender a manejar bases de dato con PostgreSQL

Ésta será la única sección del proyecto que estará en inglés. Ésto es hecho a propósito, y busca ayudar a mejorar el nivel de inglés profesional, además de que la programación y mayoría de fuentes existen todas en inglés.

**¡Ánimo!**

## Specs

- Web framework: Django
- Database: SQLite 3
- API: [cheapshark.com](https://apidocs.cheapshark.com/)
- 

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