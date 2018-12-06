# edit the URI below to add your RDS password and your Heroku URL

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'

SQLALCHEMY_DATABASE_URI = 'postgres://xxxxxxxxxx'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True 
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
