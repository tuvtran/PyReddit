# PyReddit - A Reddit clone in Python and Flask

## Set up

Make sure you have Python 3 on your systen

### Set up the virtual environment

```bash
$ virtualenv venv --python=python3
```

### Install the dependencies

```bash
$ pip install -r requirements.txt
```

### Set up environment variables

```bash
$ export APP_SETTINGS=development
```

## Usage

### Run unit tests

```bash
$ python manage.py test --type unit
```

### Launch the server

```bash
$ python manage.py runserver
```

The application can now be accessed at `http://localhost:5000`

### Access the shell

```bash
$ python manage.py shell
```
