# TO DO LIST

## Description

A to-do list using django

 ## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/yashbijoor/to_do_list-v1.git
$ cd to_do_list
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenvwrapper-win
$ mkvirtualenv env
```

Now install django in the virtual env:
```sh
(env)$ python -m pip install django
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Now you can run the server by:
```sh
(env)$ cd to_do_list
(env)$ python manage.py runserver
```
And navigate to [http://localhost:8000/](http://localhost:8000/)
