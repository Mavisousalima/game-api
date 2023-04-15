# Game Management API

This is a Django API that handle the management of a game.

## Features

The Django application includes the following features:

- User Customization: Using Django build in authentication, the API is able to create a custom user with fields such as image, health, exp, etc.
- Ranking: A view that return a ranking of the players based on EXP

## Installation

To install and run the Django application locally, follow these steps:

- Clone the repository to your local machine using git clone https://github.com/Mavisousalima/game-api.
- Navigate to the project directory: cd game-api.
- Create a virtual environment: python -m venv env (optional but recommended).
- Activate the virtual environment:
  For Windows: env\Scripts\activate
  For macOS/Linux: source env/bin/activate
  Install the dependencies: pip install -r requirements.txt.
- Run the database migrations: python manage.py migrate.
- Start the development server: python manage.py runserver.
  Access the application in your web browser at http://127.0.0.1:8000/.

# Tests

You can run the tests using:

```
python manage.py test
```
