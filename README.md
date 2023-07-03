# This project prepared for MONDOIR Interview

# Installation
## Database
### Install mysql
#### Ubuntu 22.04
##### Install mysqlserver
```
sudo apt update
sudo apt install mysql-server
sudo mysql
```
#### Create db and user for your project
```
CREATE DATABASE <db_name>;
CREATE USER '<username>'@'localhost' IDENTIFIED WITH mysql_native_password BY '<password>';
GRANT CREATE ON *.* TO 'djangouser'@'localhost';
GRANT ALL ON *.* TO 'djangouser'@'localhost';
FLUSH PRIVILEGES; #
```
#### Install mysql connector
```
sudo apt install libmysqlclient-dev default-libmysqlclient-dev
```

#### install packages
```commandline
pip install -r requiremets.txt
```

#### Migrate
```
python manage.py migrate
```

### Create superuser to connecting with django admin panel and swagger
```commandline
python manage.py createsuperuser
```

### You can run project tests
```commandline
python manage.py test
```

# Run
```commandline
python manage.py runserver 0.0.0.0:8000
```