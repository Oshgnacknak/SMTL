# SMTL

This webapp is for for the 'Stadtmeisterschaft' players
list and the singup form written in python/flask.


## Run

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
# Build from Github
docker build https://github.com/Oshgnacknak/SMTL -t smtl

# Run and set secret key, port and database uri here
docker run -d \
	-p 80:80 \
	-e PORT=80 \
	-e SECRET_KEY=secret \
	-e SQLALCHEMY_DATABASE_URI='sqlite:///:memory:' \
	--name name \
	smtl
```
