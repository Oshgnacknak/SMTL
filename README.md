# SMTL

This is a 'single page webapp' for the 'Stadtmeisterschaft' players
list and the singup form written in python/flask.


## How to Run

```sh
# Clone this repository
git clone git@github.com:Oshgnacknak/SMTL.git

# cd into it
cd SMTL

# Install dependencies
pip install -r requirements.txt

# Create config.py and change the 'SECRET_KEY'
cp config.py.dist config.py

# Execute run.py
pyhton run.py
```


## TODO

- Create any form of database for the players.
- Use a CSRF token.
