#Linux Server Configuration
Part of Udacity nanodegree.

### 1. connect to server

Open the terminal.

```
# Login to server
ssh grader@34.219.209.213 -p 2200 -i ~/.ssh/linCourse
```

# private key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0GdKD1VMSjtwdE/0C/LA5r82TjvhKf5mK5VUjiTXfAvKqe3e
guI3p1wqKbNCSYnLfbrK60J5qkiP+xHLSMjli3Nm7FD1uUKvXefDrpidIrvFHj7E
913iaNMnb7XvA7RNOq9xp1QROT+CsObaruOtfXiu7VAvNzvvUg/QAvfbaXnS4POT
u8sxOS0jbbPHaRuU+tjTDicNbjj/itas/g7aQi16FMhQThtp1VfWebYJ3PZL/Yoe
5Fw8hG58gMn9RGIMjP1TiRLpgvOy4WPg+aKC4K8H+sU8XtYxzceDPjVi+0+fDUt3
dJun4EbVcDGpXwDywm4XxAOh2EaUIoO0chmpdwIDAQABAoIBAAMuEEs7mfZoAcdE
kQy9n4Pl1wZKk5z4bMateKTSmxchdu4w2vxUR1UeauZH/fLxT1GT0BTW5tRaVxgV
pWxu5FHEaQWiFp3FDrf4GVxIp90n0FIt0wOTQykmT6u8svDzh1ol4y4SclDVT0Ez
xJJ2lucbOFAWsSG+oGA4LYxeC9MIKcOVmfwLkdWSQg4LSCyVEnPGNyVR00HbVEHm
L944pJAMN7j5uqXOCbUCmC5tEAXBm3ZueAJbHA84hootrGiBiv/pJbmLOEnkKIoR
RR1mrCvR/u1BsQJmzTnAk1qwq+G3XYdpZDJW8++pXUlINsoc9JQBFMHDjObqJhF2
tmXFFMECgYEA/Proo+8DdzOpyJsgdn5Lv6MLwI7L3s5Qs9v5XLt5BksGpuTiRfwI
F9IvqB9E42Z1eF0i3sixsFs0b/LwPhtfU7oVBbvtDCA9xiF8rOiWjiLzYtigP6IK
cT36sHR74mopawJafCOrQBPhh7753mRQFlm91VUqLK129WH1P2N01L0CgYEA0uQo
OyeEr31MJ4uTxbAf89indfHLrKh2FyUF0jQeVNAKNjWrxM7T9RJwlH32qtx8ayss
QfHoZKcHbB4uE5ggi2VNQt9WjDSEJow9bcA0g3aFsZzdwEw0S68VPn73Ts3CC2VU
aPP5CfHzZZc73t0PZ21iPZvTp7x2R8+3c+jjrEMCgYBKgQakyQ6HO6LkHrOX0igy
3yzl3+gwzSg9YCp3YgsJjG0AF+Z/3/LuOQuqAtOB+TndYeiUHh0eqC2wTqbsU5lm
iiYI00jDyncG8/PI5JL6d1agpNXFB871fOBouVWG3+ckycOmTcbwjypblSX3lilz
+6gJvRQ3pjqjl97ndT4CLQKBgQDO2/WKcKz55hF5CLQeSTBOY8l/K3n5FhUfhrU7
BtxpnNcnbWXbWnUWAsxjG1uFJVj1VhfHZ53ofN4O81uG5MWndepfGesvA6RMm2r1
6H6aJPvmyFPLd/Qj+M0BzFCQ/8rCmtY9THKPisCQedPEO1oMvYKLo/nsojPzJJBy
JZKNOQKBgQD3e0vKDjHvv6we3LuCJuZldrOBw1KNbhVyPOrw+MptfRjle32nmbY1
Eo/7kVowQ3FTOEXKxZ1o79MLxnnGAqqiLZgoEGSlMwcd/DaEa//u5UyZ/bCYquKt
7P+MUbSF08W9je1u41zYqs9QgoZRGuH7a9f5uFOlg1lgOhNKSN25Bw==
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
