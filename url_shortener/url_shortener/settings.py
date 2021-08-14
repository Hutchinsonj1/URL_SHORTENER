import os

#SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'  


SQLALCHEMY_TRACK_NOTIFICATIONS = False
ADMIN_USERNAME=os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD=os.environ.get('ADMIN_PASSWORD')


#.GET communicates with directories. .ENVIRON communicates 'with the environment'