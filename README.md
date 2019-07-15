#Linux Server Configuration
Part of Udacity nanodegree.

### 1. connect to server

Open the terminal.

```
# Login to server
ssh  grader@34.221.64.52 -i ~/.ssh/linuxCourse -p 2200
```

# private key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAw1jx5nfbWnh5kZV8poN43cBjDBaqGIa3R0TzyFKr93JrK1ot
2nT92uX/PmKnHrhXLWAvhc5h2hmu3wqEQOWlrxDkwntt4uQNPdXy5VtSmFUqZgFP
cWwh1v6R/4C5CvPS8IfBZuxL1vqc5cX0lSNO+34dVR0yYoGaUgCv1B9rv0zUzWpO
8gDY0UdHcJgosaom1uh1yDOQtdw8orLeK5eNo8DKqry4zp2VCBRu8/3QfT0G0NNt
63Yespgd+/gzUiVpY3s3KQa0d6pNbpzEwlgAxrGq+F8uh2S4hgZwrFOWYJdKCNhr
3b1Yb5K4MDX1WTyjhaTBg+PYyR46N9Wym/1ZMQIDAQABAoIBAQCjtoskZxaCf60C
gZFxy4Uj8vQPUX9EBsLbC8JzBDXyrwV5053SE3IcXdzH383HRR5qfM3XCduf+R5A
9oNYEB4G1dWh1+eD2zPturxR03MpD1b1HewCVmkV0UtyIeLydt01j9BZ/XahuG59
cqVDx8+NnWffyRRM0ekPCFxTHfIi4zyfhXVtGGOQWKayQDq6g3ZR255e0sRx95Ut
L62S4HjMXVE8Uyk9ebH+ucwLfyxWlSXPEnvZi/k1XCqkXiHavN60z1S1wZZacINY
z3ar30LoacmRmbxziY+Qu6iE95bgNMPPtoXZ8FdbJkmBIgG4/7c9y0JpPskQdo4G
2vt95C6xAoGBAPUDIo08xI7XQJQcaq7pmceAz5WSTZtXKp3arNvp7AUcS80nYcKm
AYNdl06zdZEyF76RSXr7YQbxjlV1qYrhdszN9vWpgV9FL2pDDAZcnM5GHZOW62+j
4zA74qrsXgr0ELmi1aOT/7bXO51z+2HM4g01cnVLiSkVVZ7gisiS4oRvAoGBAMwb
of0rlCxnaMDjWXiJyHCwC5AfmEXHHlGEaqLOZ1XVFJy+Tj01Lj1wozimphQMz99b
OUgabHIKW8K+Fhm8QH5pCpQRLN3k+4Dt10Hu+pxrhrbh6YKIRZPgHYCT8Ldxd8xH
1Ya3E8djg6kQ2x/sU4BX+l1tF6aNNgj/gyImVwxfAoGAM7FUod3XTpfFjTotm/e3
NStNIK58ZzDN0f4oCEHjRPTCXWdYrdueaBvf53/fZyHddpxql2LgBroCIK+xdJa7
HNy7pPr9S59qMI4yxEjX4IFUjiYCSEyYiz2nRg6WjNMPkEr1rgx0oBvq/P5SZED4
1HaZTnwAVUWmCd4wCb9LwUsCgYA+KcxURwmB3JzS4mtFgvFBINzksDq4RcS+Hw47
N5HRWmxEsNEzYxcKL1wGzPqX8K7+39G6XBHbSbxYu3wPqn4aAfPu1KxNiIfw5H9C
3X4GVdlZqcRstQQ73W4e0u/lbvGFjftCZE/p0i0vOKsENf3YgPMHsUoat7dVVjyi
EftBEQKBgQDIfJQ6en5qFbaU8Bnz9KrKrsJ4kPEf6vVG2HSbPc1CPWBb/WuMvm7T
5wLdnFGUGwweObM5eDk6ioSBkHcglKp1b+XkX9NbQqpNEeATtq2CwqwPDFmz75wb
oTNcdaRUg3qJgvaAgLfxZv7Tsds8rkoe+LnmXmX6EkvIM0b0Vx9UCQ==
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
linuxCourse
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
clone inside  ``/var/www/html``

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

## Resources
https://knowledge.udacity.com/questions/31565
