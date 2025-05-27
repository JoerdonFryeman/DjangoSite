# Website template
### Example of a simple Django website
Run the following commands to bootstrap your environment
```console
git clone https://github.com/JoerdonFryeman/DjangoSite.git
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
### Deploy on PythonAnywhere
Bash console
```console
pwd
git clone https://github.com/JoerdonFryeman/DjangoSite
mkvirtualenv --python=/usr/bin/python3.10 venv
python3 -m pip install --upgrade pip
```
Files
/home/JoerdonFryeman/DjangoSite/website/website/urls.py -> comment this line:
```python
# from website.settings import dev
# from django.conf.urls.static import static

# path('**debug**/', include('debug_toolbar.urls'))

# if dev.DEBUG:
# 	urlpatterns += static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)
```
home/JoerdonFryeman/DjangoSite/website/website/settings/dev.py -> comment this line:
```python
# INSTALLED_APPS += ['debug_toolbar', ]
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
```
/home/JoerdonFryeman/DjangoSite/website/website/settings/prod.py -> your website
```python
address: ALLOWED_HOSTS = ['*']
```
Bash console
```console
pip install -r /home/JoerdonFryeman/DjangoSite/website/requirements_prod.txt
cd /home/JoerdonFryeman/DjangoSite/website/
cp .env.template .env
python3 manage.py collectstatic
```
Web-page

Source code: /home/JoerdonFryeman/DjangoSite/website/manage.py

Working directory: /home/JoerdonFryeman/DjangoSite/website/

Virualenv: venv

Static files:

/static/ /home/JoerdonFryeman/DjangoSite/website/static/

/media/ /home/JoerdonFryeman/DjangoSite/website/media/

WSGI configuration file:
```python
import os
import sys

path = '/home/JoerdonFryeman/DjangoSite/website/website'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
### Support with Bitcoin
bc1qewfgtrrg2gqgtvzl5d2pr9pte685pp5n3g6scy
