# Website template

Example of a simple Django website

## Quickstart

Run the following commands to bootstrap your environment

```console
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

Bash console

```shell
pwd
git clone https://github.com/Kepler54/DjangoSite
mkvirtualenv --python=/usr/bin/python3.10 venv
```

Files

/home/Kepler54/DjangoSite/website/website/urls.py -> comment this line:

```
# from website.settings import dev

# path('**debug**/', include('debug_toolbar.urls'))

# if dev.DEBUG:
# 	urlpatterns += static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)
```

home/Kepler54/DjangoSite/website/website/settings/dev.py -> comment this line:

```
# INSTALLED_APPS += ['debug_toolbar', ]
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

```

/home/Kepler54/DjangoSite/website/website/settings/prod.py -> your website

```shell
 address: ALLOWED_HOSTS = ['*']
```

Bash console

```shell
pip install -r /home/Kepler54/DjangoSite/website/requirements_prod.txt
cd /home/Kepler54/DjangoSite/website/
cp .env.template .env
python3 manage.py collectstatic
```

Web-page

Source code: /home/Kepler54/DjangoSite/website/manage.py Working directory: 

/home/Kepler54/DjangoSite/website/ Virualenv: venv

Static files:

/static/ /home/Kepler54/DjangoSite/website/static/
/media/ /home/Kepler54/DjangoSite/website/media/

WSGI configuration file:

```
import os
import sys

path = '/home/Kepler54/DjangoSite/website/website'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
