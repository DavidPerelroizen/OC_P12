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

### Run the server

Open your terminal and run the following command:
```bash
python .\epicevent\manage.py runserver
```

### Test the APIs

Once the terminal command is executed, you can test the endpoints through different ways

#### Use the Postman collection

Follow the link below.
```bash
Link to postman collection:
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
