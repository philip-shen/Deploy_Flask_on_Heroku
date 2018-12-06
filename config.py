# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'

# Uncomment the line below if you want to work with a local DB
'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
'''
SQLALCHEMY_DATABASE_URI = 'postgres://hqboudhwqrclro:8e709b9029a75f42c7afc807ac529af286224ee89deb78315e68e80b92675d4f@ec2-54-235-193-0.compute-1.amazonaws.com:5432/dbnccqn9dvatk6'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True 
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
