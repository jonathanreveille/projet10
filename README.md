# P10
Project 10 OpenClassrooms Course
# Project 10 - Openclassrooms Python Course :

## Search for a product that you eat often and check out for healthier suggestions !

### What is in this project ?
- Use of Django Framework.
- Use of OOP and Python 3.7.
- Use of OpenFoodFact API services.
- Use of Bootstrap 4.
- Database (for production): SQLite3.
- Determinate a strategy for testing the application (in prod)
- Project is tested, coverage will reach upto 80% (goal - in prod)
- Test includes : Unit tests, integration tests (in prod)
- Use of pipenv (virtual env.)
- Respect and follow recommendations from PEP8 (style guide),
 PEP257(docformatter)

## The project

This project is set for production use. The application is
deployed on Digital Ocean.
 
### Structure of the code

##  Getting started

If you want to run this project, clone this project, and start you favorite editor (example: VisualCode).

First of all, you need to **install pipenv**.
* `pipenv install` (it installs all the requirements), once loaded, don't
forget to activate a shell with `pipenv shell` in your terminal to activate the environment.
The **advantage** of pipenv is that it is cross-platform. It is 
recommended by the official documentation for python's virtual
environment.

Secondly, the current local database might be empty, to feed it you may do these next steps :
* 1st step : `python manage.py makemigrations` or for a specific app ``python manage.py makemigrations <app_name>`(for example app_name is "products" for this project Purbeurre)
* 2nd step : `python manage.py migrate`
* 3rd step : `python manage.py initdb`- loads product in your database

Thirdly, run the command in your terminal to check if the application works locally first :
Place yourself at the root of the project and run :
* `python manage.py runserver`
* You may connect yourself at this adress on your web browser : http://localhost:8000/ or click on
the link that is presented on your terminal screen.
* You can stop the server by doing `ctrl+c` in the server.

If you need to delete all the entries if the database (when you are in development mode), you may :
* 1st step : `python manage.py deletedb`
* 2nd step : delete the file at the path : purbeurre.products.migrations.0001_initial.py
Becareful not to delete the "____init____.py", nor the folder migrations ! 
* 3rd step : You may add more categories, or, change the models and its fields, at this moment.

### RUN Test
* Simply run this command in your terminal in the project : `python manage.py test --verbosity 2`
* if you want to use coverage, the command is : `coverage run --source="." manage.py test`

## Acknowledgment
I would like to thank my mentor, Thierry Chappuis, for all the help
and advices he gave to me to accomplish this project.