# Flask study

## Gunicorn

```sh
gunicorn hello:app
```

### with Config File

```sh
gunicorn -c gunicorn.conf.py hello:app
```


### with Log config file

```sh
gunicorn --log-config logging.conf hello:app
```
