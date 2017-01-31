# Real Time Notification using Django, Socket.io, Redis

Environment
--------
**Vagrant and VirtualBox**
  * config.vm.box = "bento/ubuntu-14.04"
  
**Installing Dependencies**
```
$ sudo apt-get install curl python-software-properties g++ make
$ sudo apt-get install python python-virtualenv
$ sudo apt-get install redis-server
$ sudo add-apt-repository ppa:chris-lea/node.js
$ sudo add-apt-repository ppa:nginx/stable
$ sudo apt-get update
$ sudo apt-get install nodejs nginx
```

Move directory into `nodejs_notifier` and install nodejs modules, these script will automatically added into `node_modules`
```
$ curl https://www.npmjs.org/install.sh | sudo sh
$ sudo npm install --save socket.io
$ sudo npm install --save cookie
```

Install Python dependencies
```
$ pip install django
$ pip install django-notifications-hq
$ pip install django-user-sessions
$ pip install redis
```

Features
--------
* Django Admin
* Integration with Django Notification HQ
* Redis Server

Running App
--------
```
$ python manage.py migrate # to sync db
$ python manage.py runserver
```

Testing Functionality
--------
* Create super user
```
$ python manage.py createsuperuser
```
* Login into different browser to /realtime using same account and send notification
