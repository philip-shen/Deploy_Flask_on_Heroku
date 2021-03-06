#2018/11/25 Add class DellTest():

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
'''
app.config.from_object('config')
db = SQLAlchemy(app)

class PictureDate(db.Model):
    __tablename__ = 'PictureDate'
    Id = db.Column(db.Integer, primary_key=True)
    Uuid = db.Column(db.String(64), unique=True)
    Title = db.Column(db.String(64))
    Description = db.Column(db.String(128))

    def __init__(self
                 , Uuid
                 , Title
                 , Description
                 ):
        self.Uuid = Uuid
        self.Title = Title
        self.Description = Description

class GoogleDrive_callputjpg(db.Model):
    __tablename__ = 'CallPutJPG'
    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    title1 = db.Column(db.String(86))
    modifiedDate = db.Column(db.String(26))
    
    def __init__(self
                 , title
                 , title1
                 , modifiedDate
    #             , Remark
                 ):
        self.title = title
        self.title1 = title1
        self.modifiedDate = modifiedDate

class BulkInsertTest():
    def __init__(self,db,dbmodel_class):
        self.db = db
        self.dbmodel_class = dbmodel_class

    """Batched INSERT statements via the ORM in "bulk", discarding PKs."""
    def test_bulk_save(self,list_folderfiles):
        
        self.db.session.bulk_save_objects([
                #GoogleDrive_callputjpg(
                self.dbmodel_class(    
                title=dic_files['title'],
                title1=dic_files['title1'],
                modifiedDate=dic_files['modifiedDate']
                )
                for dic_files in list_folderfiles
        ])        
        

    """Batched INSERT statements via the ORM "bulk", using dictionaries."""
    def test_bulk_insert_mappings(self,list_folderfiles):

        self.db.session.bulk_insert_mappings(self.dbmodel_class, [#GoogleDrive_callputjpg, [
                    dic_files
                    for dic_files in list_folderfiles 
        ])        

'''***7.3  Using SQLAlchemy ORM (Object-Relational Mapper)***
http://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python3_Flask.html#zz-7.
****Flask-SQLAlchemy how to delete all rows in a single table***
https://stackoverflow.com/questions/16573802/flask-sqlalchemy-how-to-delete-all-rows-in-a-single-table'''
class DellTest():
    def __init__(self,db,dbmodel_class):
        self.db = db
        self.dbmodel_class = dbmodel_class
    
    def del_all(self):
        try:
            num_rows_deleted = self.db.session.query(self.dbmodel_class).delete()
            #self.db.session.commit()            
        except:
            self.db.session.rollback()

        return num_rows_deleted    

    def del_filterby_title(self,str_title):
        try:
            '''#for specific value
                db.session.query(Model).filter(Model.id==123).delete()'''
            instances_to_delete = self.db.session.query(self.dbmodel_class).filter_by(title=str_title).all()
            for instance in instances_to_delete:
                self.db.session.delete(instance)

            #self.db.session.commit()
        except:
            db.session.rollback()    


#2018/11/22 Fast SQLAlchemy counting (avoid query.count() subquery) 
#           https://gist.github.com/hest/8798884
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count

#if __name__ == '__main__':
#    manager.run()