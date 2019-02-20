# Simple Wealth
Online Brokerage Service that uses Recommendation Systems

## Environment Setup
We recommend using a python virtual environment to run our application. This will avoid potential issues where the required packages conflict with the packages install on the system python distribution. Python 3.6 has been used throughout our development.

### Virutal Environments
Run the following commands to install python virtual envrionments and create a new one.

```bash
$ sudo apt install virtualenv
$ python3 -m venv ~/simple-wealth-env
```

Activate the virtual environment you just created and install the required packages found in the root of this repository in **requirements.txt**.

```bash
$ source ~/simple-wealth-env/bin/activate
$ pip install -r requirements.txt
```
When you are done you can simply use the `deactivate` command to switch back the system python.

## Running the Application
Start from the root of the repository. Make sure you have activated the correct virutal environment.

```bash
$ cd simple-wealth
$ python manage.py runserver
```

Now that the server is running you can go to your browser and enter http://localhost:8000/. You have now entered _Simple Wealth_!
