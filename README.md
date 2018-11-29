# Deploy_Flask_on_Heroku
Deploy a flask APP on Heroku.

## DB Operation
Step 1.
``` 
(Flask_trial) d:\project\Python\Deploy_Flask_on_Heroku>python dbcreate.py db init
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRAC
K_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to sup
press this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
Error: Directory migrations already exists
``` 

Step 2.
``` 
(Flask_trial) d:\project\Python\Deploy_Flask_on_Heroku>python dbcreate.py db migrate
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRAC
K_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to sup
press this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'CallPutJPG'
INFO  [alembic.autogenerate.compare] Detected added table 'PictureDate'
Generating d:\project\Python\Deploy_Flask_on_Heroku\migrations\versions\4663c0d429d6_.py ... done
``` 

Step 3.
``` 
(Flask_trial) d:\project\Python\Deploy_Flask_on_Heroku>python dbcreate.py db upgrade
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 64a46080374d -> 4663c0d429d6, empty message
``` 

Step 4.
``` 
(Flask_trial) d:\project\Python\Deploy_Flask_on_Heroku>python dbInsert.py
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
Google Authentication Started
Google Authentication Completed!
Insert 1038 rows into table.
SA ORM Bulk insert, using dictionaries- total time: 0.40 seconds
``` 

Step 5. Enjoy it.

![alt tag](https://imgur.com/yoSxIRg.jpg)

## Upload to Heroku
Step 1. heroku git:remote -a

![alt tag](https://imgur.com/AdDZgLY.jpg)

Step 2. Log on Heroku.

![alt tag](https://imgur.com/L1cnYWk.jpg)

Step 3. Enjoy it on Heroku.

* [Heoku Demo](https://marvelcomics-excelsior.herokuapp.com/)

## Environment Configuration
* Windows 10
* Python 3.6
* Refer requirements.txt to pip necessary modules.

## Reference 
* [Flask-Migrate-Tutorial 透過 Flask-Migrate-Tutorial 管理資料庫 (database)](https://github.com/twtrubiks/Flask-Migrate-Tutorial)
* [Deploying-Flask-To-Heroku 今天教大家如何佈署 Flask App 到 Heroku](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)
* [flask_sqlalchemy_bulk_insert Performance test of bulk insert that inserts multiple rows from Google Drive by flask sqlalchemy](https://github.com/philip-shen/flask_sqlalchemy_bulk_insert)
* [w3schools](https://www.w3schools.com/default.asp)