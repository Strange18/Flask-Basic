# Flask-Basic

This repo contains the basic implementation of Flask. 
The code in this repo connects with the [Elephant SQL](https://www.elephantsql.com/) a hosted Postgres server.

First, create a virtual environment.

```
virtualenv env
```
Then activate the environment.
```
source env/bin/activate
```

Install all the requirements.

```
pip install -r requirements.txt
```
To run the application 
```
python3 app.py
```

Also, create a .env file locally that contains all the credentials provided by Elephant SQL.
