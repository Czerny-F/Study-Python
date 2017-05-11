# Study-Python
on Study

# Django
```
$ pip install Django
$ python
>>> import django
>>> print(django.get_version())
1.11.1
```

```
$ django-admin startproject mysite
$ cd mysite
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

May 11, 2017 - 09:19:37
Django version 1.11.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

```
$ python manage.py startapp polls
```

# References
- [Python 3.6.1 ドキュメント](https://docs.python.jp/3/)
- [Python Boot Camp Text](http://pycamp.pycon.jp/)
- [CODEPREP](https://codeprep.jp/books/61)
- [Pythonを書き始める前に見るべきTips](http://qiita.com/icoxfog417/items/e8f97a6acad07903b5b0)
- [DJANGOPROJECT.JP](http://djangoproject.jp/)
