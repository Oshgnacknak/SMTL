# SMTL

This webapp is for for the 'Stadtmeisterschaft' players
list and the singup form written in python/flask.


## How to Run

```
# Clone this repository
git clone git@github.com:Oshgnacknak/SMTL.git

# cd into it
cd SMTL

# Install dependencies
pip install -r requirements.txt

# Create config.py and edit it to your likings
cp config.py.dist config.py

# Execute run.py
pyhton run.py
```

## Docker 
```
docker run --rm -p 5000:5000 -e SECRET_KEY=secret -e SQLALCHEMY_DATABASE_URI='sqlite:///:memory:' --name name smtl
```
