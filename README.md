#Item Catalog
Part of Udacity nanodegree.

## 1. how to start
### 1. Setup: Configure VM & Database

**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org). 

**Step 2:** Download the VM configuration from the [downloads folder](downloads/) or clone from this [github repo](https://github.com/udacity/fullstack-nanodegree-vm). 

**Step 3:**  Download all files from the current folder. Then, copy them to the `vagrant/`.

**Step 4:** Open the terminal. Then, run the following commands:

```
# Install & Configure VM
cd /path/to/vagrant
vagrant up

# Log into machine
vagrant ssh

```

### 2. Run

Open the terminal.

```
# Launch & Login to machine
cd /path/to/vagrant
vagrant up
vagrant ssh

cd /vagrant 

# Run
python lotsOfCategories.py
python application.py
```

## Rubric

|SECTION|CRITERIA|
|---|---|
| API Endpoints | The project implements a JSON endpoint to get all categories with its items, get single category items and get single item |
| CRUD: Read | reads category and item information from a database|
| CRUD: Create | includes a form allowing users to add new items .|
| CRUD: Update |  include a form to edit/update a current record in the database table|
| CRUD: Delete | include a function to delete a current record |
| Authentication & Authorization | Create, delete and update operations do consider authorization status prior to execution.Page implements a third-party authentication & authorization service like ``Google Accounts``.there is a 'Login' and 'Logout' button/link in the project|
| Code Quality | the code use pep 8 style code|
| Comments | Comments are present|