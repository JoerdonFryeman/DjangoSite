# Website template

Example of a simple Django website

## Quickstart

Run the following commands to bootstrap your environment

```console
sudo apt-get install python3-venv python3-pip
git clone https://github.com/Kepler54/DjangoSite
cd DjangoSite

python3 -m venv dvenv
source venv/bin/activate
pip install -r requirements/dev.txt

cp .env.template .env
```

Run the app locally:

runserver --settings=website.settings.dev

Run the app with gunicorn:

gunicorn website.wsgi -b 0.0.0.0:8001

## Deploy on PythonAnywhere

Console-page

```console

pwd
git clone https://github.com/Kepler54/DjangoSite
mkvirtualenv --python=/usr/bin/python3.10 venv
pip install -r requirements_prod.txt
python3 manage.py collectstatic
gunicorn website.wsgi -b 0.0.0.0:8001

```

Web-page

Virualenv: venv

Source code: /home/Kepler54/DjangoSite/website/manage.py
Working directory: /home/Kepler54/DjangoSite/website/

Static files:

/static/
/home/Kepler54/DjangoSite/website/static/

/media/
/home/Kepler54/DjangoSite/website/media/

WSGI configuration file:

```code

import os
import sys

path = '/home/Kepler54/DjangoSite/website/website'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

Files-page

ALLOWED_HOSTS = ['*']

/home/Kepler54/DjangoSite/website/website/urls.py
# path('__debug__/', include('debug_toolbar.urls'))
