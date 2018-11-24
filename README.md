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

Step 3.
``` 
(Flask_trial) d:\project\Python\Deploy_Flask_on_Heroku>python dbcreate.py db upgrade
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 64a46080374d -> 4663c0d429d6, empty message

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

## Environment Configuration
* Python 3.6
* Refer requirements.txt to pip necessary modules.
