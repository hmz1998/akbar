# Django Project Creation Version 3.1.1

Project Stack:

|    Name  |  Version   |
|:---------|:----------:|
| Python   |  3.8.5     |
| Django   |  3.1.1     |
| Git      |  2.17.1    |
| Nginx    |  1.14.0    |
| Ubuntu   |  18.04     |
| Postgres |  10.14     |
| Redis    |  4.0.9     |

***




Before creating django project you must first create virtualenv.

``` sh
$ python3.8 -m pip install virtualenv
$ python3.8 -m virtualenv venv
```

To activate virtualenvironment in ubuntu:
```
$ source venv\bin\activate
```

To deactive vritualenvironment use:
``` sh
$ deactivate
```

After activation must install all packages:
```sh
pip install -r requirements.txt
```

## Getting Started


1. Create django application or clone it from git.

```sh
$ django-admin startproject kernel .
```

```sh
$ git clone <git_address>
```
2. config setting from ***settings-template.ini***

3. Database Creation Commands:

``` sql
CREATE USER bio WITH PASSWORD '1234';
CREATE DATABASE bio;
ALTER ROLE bio SET client_encoding TO 'utf8';
ALTER ROLE bio SET default_transaction_isolation TO 'read committed';
ALTER ROLE bio SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bio TO bio;
```

4. To get beatiful django-admin do bellow instructions:

```sh
$ python manage.py loaddata admin_interface_theme_uswds.json
```

Then modify ***base_site.html*** from:
```sh
$ python manage.py loaddata admin_interface_theme_uswds.json
# ------------------------------------------
$ nano <project_name>\venv\Lib\site-packages\django\contrib\admin\templates\admin\base_site.html
```
replace first line with bellow syntax:
```python
{% extends "admin_interface:admin/base_site.html" %}
```

5. To create all database tables:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

6. Deployment Check
```sh
$ python manage.py collectstatic
$ python manage.py check
$ python manage.py test
$ python manage.py check --deploy
```

### NOTES:
* if rcssmin or jsmin in django compressor doesn't install do bellow commands:

```sh
$ pip install rcssmin --install-option="--without-c-extensions"
$ pip install django-compressor --upgrade
$ pip install rjsmin --install-option="--without-c-extensions"
```

* If **psycopg2** doesn't install in ubuntu OS:
```sh
$ pip install psycopg2-binary
```
