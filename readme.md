 # EPICEVENT app

The EPICEVENT app aims at providing to the users a secured CRM app enabling them to manage clients, contracts and events
while making sure that each user has only the appropriate access level for each view and object. The app is also providing
an administration interface helping to manager users and any existing object in the database. A collection of endpoints
are enabling the authorized user to operate different CRUD operations from other apps or devices.

This app is using DJANGO as base framework, DJANGO REST FRAMEWORK for APIs management, and JWT for authentication.
The database used is PostgreSQL.


## Installation

Below the instructions will be given to properly proceed to the needed packages installing.

### Virtual environment configuration

**Install the virtual environment package**

```bash
pip install virtualenv
```

**Create the virtual environment**

```bash
virtualenv localdir
```

You must specify the local directory path

**Activate the virtual environment**

Mac OS/Linux
```bash 
source localdir/bin/activate
```

Windows
```bash
localdir/Scripts/activate
```

### Install the necessary packages

All necessary packages are contained in the requirements.txt.
Install them all by running the following command in terminal.
```bash
pip install -r requirements.txt
```

## PostgreSQL configuration

### Get postgreSQL

Follow the link: https://www.postgresql.org/download/

Then, select your operating system and follow the installation protocol.

### Create postgreSQL DB

Create a new database noting carefully the username and the password you used for the creation and the database name.

### Update the settings.py

Open the settings.py file:
```bash 
epicevent/epicevent/settings.py
```
Change the database settings with the following template code:
```bash
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '<your_db_name>',
       'USER': '<your_db_username>',
       'PASSWORD': '<your_db_password>',
       'HOST': '<your_db_hostname_or_ip>',
       'PORT': '<your_db_port>',
    }
```

### Before making the first migrations

Open the file ``epicevent/authentication/models.py``

Comment out the four lines displayed below:
```bash
administration_group, created = Group.objects.get_or_create(name='administrators')
sales_group, created = Group.objects.get_or_create(name='salesmen')
support_group, created = Group.objects.get_or_create(name='supporters')
groups_names_list = [administration_group.name, sales_group.name, support_group.name]
```

### Run migrations

Run the following commands in your terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```
Once migrations are done, de-comment the lines from the step above and re-migrate.

## Usage

### Create a superuser

In order to access to django's administration panel a superuser profile must be created.
Run the following commands in your terminal and follow the instructions: ``python manage.py createsuperuser``

### User permissions

Users are split into three groups:
- administrators
- salesmen
- supporters

Permissions summary is displayed in the table below:

| Groups \ Objects        | User           | Contract  | Event | EventStatus | Client |
| :-------------: |:-------------:| :-----:| :-------------:| :-------------:| :-------------:|
| administrators      | CRUD | RUD | RUD | CRUD | RUD |
| salesmen      | not allowed      |   CR(UD) | CR(UD) | not allowed      | CR(UD) |
| supporters | not allowed      | R | R(UD) | not allowed      | R |

*(UD) : the group member as access for update and delete actions only to the objects he is directly linked to*

### Run the server

Open your terminal and run the following command:
```bash
python .\epicevent\manage.py runserver
```

Use the following link to access to the admin panel: ``http://127.0.0.1:8000/admin/``
Log in using your superuser credentials.

### Test the APIs

Once the terminal command is executed, you can test the endpoints.

Follow the link below to access the Postman collection.
```bash
https://go.postman.co/workspace/New-Team-Workspace~23c58d19-ba3e-4393-97fe-d94ea4106519/collection/20673323-4517d629-0305-4bef-849a-502f221ffc17?action=share&creator=20673323
```

#### Use Swagger for APIs

Follow the link below for swagger API documentation.
```bash
http://127.0.0.1:8000/swagger/
```

Follow the link below for swagger API documentation with redoc layout.
```bash
http://127.0.0.1:8000/redoc/
```

## Flake8 set-up and checks

### Flake 8 configuration

In the project directory, create a file as follows:
```bash
setup.cfg
```

In this file, write the following:
```bash
[flake8]
max-line-length = 119
exclude = venv, __init__.py, *.txt, *.csv, *.md
```
We restrict the maximum number of characters per line at 119. So flake8 won't consider as errors a line as long as it
has fewer characters.
We exclude from the flake8 checks the followings:
- Our virtual environment libraries
- Our packages init files
- Our requirement file
- Our readme file
- Our CSV databases
- Our migrations files


### Execute flake8 report

In case the user requests a regular flake8 check on the terminal, proceed as follows:
```bash
flake8 path/to/project/directory
```
