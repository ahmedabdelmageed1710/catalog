#Linux Server Configuration
Part of Udacity nanodegree.

### 1. connect to server

Open the terminal.

```
# Login to server
ssh grader@35.156.110.233 -p 2200 -i ~/.ssh/linCourse
```

# private key
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,0C389B419E3B5368952D5655353B19E6

Oaf5tVzbTCbNctE6u2wSf2AT7oNhYf8P3azs2Joz5GsJwGHLaFwaUKrSRi1GqYfd
CprsMoWy4Zz5o8+AXMtSfBli3x4J5IGZzuFJf3cbOUr8Z8Wyswl0l0zZKOI9+uYR
JckrgOnQ88tQlHChLj3I2v987sqCW7jAKRQBt38xXdW7YvDzGLSvXWdAlHyYnPAb
hZnS5MnoCwKgJo4/Tos8e0w+Y4KK6EdDfEjPxLt6hEYlHqd5iWAK+yemeP1+bKHz
j4j7OSxm+B6jMfMJrbMj8QmpudFEX9zE97f2w8tnT86RxYC4kHDt2+axntZshTGN
KOdXqfvjKolqpgam7aY1Os1cyl0gDNZUiLLAuJJeArkfzCl0xJXb4bKlG1jDNTOc
kFJueu8wIt7hYQ2wtnSNXfvAU4ZXfeZZbO63YpQupOwjDWEFkxu5OiXVXmtq3L8/
YpNsuz+bjx+GTHqO1FZFiQfqsYEQzD69gJRgBky4eptU78qqPJ3cmv4CQ7QKGzwY
TvAHkHwcHq436op5sMN7l0uilb8/52siHgQYvCRaDK/IVof2MqFcPYCSgVt8PWTT
TXLGqqIGkJ1XxzmH3Uxf8ZsJ2N+i9IxMYDgjO4AAeT++md7OPuedlqytuJftGq4A
Ctnmy3+gHp7o3d3ZdCR8cao76MP5SPxz04bEMyaXIII98w0U68ayZpAIvbfl83LT
qJhuj3+d1hFPwVTRzy3NszDXAFBvaPbFxruQyArwEhEzK9T0J+UFqh3TRiT45hxV
LRZTwOPgCF/VVqh6XaphQtqwSjmsVWVcVhGvZRXJaG9lSJ0lM3tarC5FEv4L/BLg
8IY82piC4yten+GxPEAOPeGutv1AwA/Qgowo7y32bYdLtlezZ+18JIqiqD74gfJj
ROP54asRLYwCpkwqtCVzaMTyzQkAy+CHzsV+y/X3Cd544g7zZ1489ycLTiesOEBp
Q+Z/urp6quEq5Y5u02EyUIREPoHV/Ig+KsJ7mH9XmBKFCEzr+ts08Kv1q6b7bSmN
huVCt7IhomVHCXZAq85R8nqSuk7HECdWehTgtCciq99IL+zuBPtxb+lbz6V8ckQB
PD9QoVZhgfI21epS06a3HKoFih9rx9DoTHSbPw7wp7/qXV8X51Srq7x9EIG+6arw
x+NZiHOtHoWBaWZuTbYbYnQpa3edKhyo8NMNElHj5gYZQf1nkhSf5GQoOiA1RlDH
FMqadZ3DIJJhgpqTXm4miUp2S4NjkrUqS/OUtRypk9cS3d7/8NYSzwgS/OT6Dm6m
MQI5tpuqrCu7a3qB7eQv/LYe3C8P5YVILpht+qBA598sBdKcTb/0hlDb0E9Ewjdg
b2ThgPCFAM3NFqBy7I0R5FxkOm3qPBYppQfVnycLGvZ15jboGhqsn2vUNfmDPgNc
do4Xpx3FFeZvpdUVSIbNe2NTZOAYz65UFxeJW+JI4nltEvnqdilD6xOMmkuUQgfH
GfMhBz1bZt7nuoz+4vpZli2WqRQ5k7htXkuBphAA0iNWEtV0L+rRA+JWkA0a1qCs
a0TdvjMSEHKFoyoRH1OuCfYlrjiMCwdIDSjhf0AyniK9ikjmnijPP4cf3mAjuigQ
-----END RSA PRIVATE KEY-----
```

# passphrase for key
```
grader
```

#Configuration

### Install apache
```
sudo apt-get install apache2
```

### Installing mod_wsgi
```
sudo apt-get install libapache2-mod-wsgi
```

### edit
```
/etc/apache2/sites-enabled/000-default.conf
```
adding
```
WSGIScriptAlias / /var/www/html/catalog/application.wsgi
```
then
```
sudo apache2ctl restart
```

### Installing PostgreSQL
```
sudo apt-get install postgresql
```

### Installing git
```
sudo apt-get install git
```

### add user
```
sudo add user grader
```

### Giving Sudo Access
create
```
/etc/sudoers.d/grader
```
add
```
grader ALL=(ALL) NOPASSWD:ALL
```

### Generating Key Pairs
run on your local machine
```
ssh-keygen
```
give it name
```
linCourse
```
add this public key inside my server at
```
/home/grader/.ssh/authorized_keys
```
and run
```
chmod 700 .ssh
chmod 600 .ssh/authorized_keys
```

### to handle permissions
```
sudo chown -R grader.grader /home/grader/.ssh
```

### ports
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 2200/tcp
sudo ufw allow www
sudo ufw allow ntp
sudo ufw enable
```

### edit 
```
/etc/ssh/sshd_config
```
change ssh port from (22) to (2200) and edit (PermitRootLogin) set to (no)


### connect to sesrver localy

### add postgres user
```
sudo -u postgres createuser -P catalog
```

### create catalog database
```
sudo -u postgres createdb -O catalog catalog
```

### clone
clone inside ** /var/www/html **

### run
```
sudo pip install httplib2
sudo pip install requests
sudo pip install oauth2client
sudo pip install sqlalchemy
sudo pip install flask
sudo pip install psycopg2
```


# Third-party Authentication

```
using Google Accounts
```

## Rubric

## User Management

|SECTION|CRITERIA|
|---|---|
| Login To Server as grader User | can login to server as grader user using the submitted key |
| Remote Login Disabled | You cannot log in as root remotely|
| Sudo Access | grader User Has Sudo Access|

## Security

|SECTION|CRITERIA|
|---|---|
| SSH, HTTP, and NTP | Only allow connections for SSH (port 2200), HTTP (port 80), and NTP (port 123) |
| Required RSA keys | users required to authenticate using RSA keys|
| Applications up-to-date | All system packages have been updated to most recent versions|
| SSH hosted on non-default port | SSH is hosted on non-default port|

## Application Functionality

|SECTION|CRITERIA|
|---|---|
| Web Server Running On Port 80 | Only allow connections for SSH (port 2200), HTTP (port 80), and NTP (port 123) |
| Database Server | Database server has been configured to serve data (PostgreSQL)|
| web server been configured to serve the Item Catalog application | Web server has been configured to serve the Item Catalog application as a WSGI app|
| SSH hosted on non-default port | SSH is hosted on non-default port|

## Documentation

|SECTION|CRITERIA|
|---|---|
| Web Server Running On Port 80 | Only allow connections for SSH (port 2200), HTTP (port 80), and NTP (port 123) |
| Database Server | Database server has been configured to serve data (PostgreSQL)|
| web server been configured to serve the Item Catalog application | Web server has been configured to serve the Item Catalog application as a WSGI app|
| SSH hosted on non-default port | SSH is hosted on non-default port|