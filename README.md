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
