TO RUN THIS APP:

Open the Command Prompt on your computer

cd into 'production' then into 'Production1'

You may need to install the follow pckgs if you haven't already:
pip install flask
pip install flask-sqlalchemy
pip install python-dotenv

Then execute:
flask run

WHAT I CHANGED:
I MADE SURE all the files were in a folder ALSO named url_shortener INSIDE url_shortener. 
THEN made sure .env and .flaskenv were out of this folder (with the other URL_SHORTENER2 this wasn't the case)
You SHOULD be able to leave your settings variable 'SQLALCHEMY_DATABASE_URI' to the 'os.environ.get('DATABASE_URL')'
    BUT you may need to occasionally bring in the sqlite3 model in its place...:
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'