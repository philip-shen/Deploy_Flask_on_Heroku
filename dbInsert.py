from dbModel import *
from models.googleDrive import  *
from models.readConfig import *
from pydrive.drive import GoogleDrive


class GDrive_MoneyHunter():
    
    def __init__(self,list_foldersfiles,db,dbmodel_class):
        self.list_foldersfiles=list_foldersfiles
        self.db=db
        self.dbmodel_class=dbmodel_class

    # bulk insert atonce then commit
    def DB_Insert(self):
        starttime=time.time()
        
        for dic_folderfiles in self.list_foldersfiles:
            try:
                BulkInsertTest(self.db,self.dbmodel_class).test_bulk_insert_mappings(dic_folderfiles['list'])
            except KeyError as error:
                print(error)
            except Exception as exception:
                print(exception)

        self.db.session.commit()
        duration = time.time() - starttime
        #q = self.db.session.query(GoogleDrive_callputjpg)
        q = self.db.session.query(self.dbmodel_class)
        print('Insert {} rows into table.'.format(get_count(q)))
        print('SA ORM Bulk insert, using dictionaries- total time: {:.2f} seconds'.format(duration))

    def DB_DeleteAll(self):
        starttime=time.time()

        num_rows_deleted = DellTest(self.db,self.dbmodel_class).del_all()

        self.db.session.commit()
        duration = time.time() - starttime
        print('SA ORM Bulk delete {} row(s)- total time: {:.2f} seconds'.format(num_rows_deleted,duration))

if __name__ == '__main__':
    configPath = 'config.ini'
    localReadConfig = ReadConfig(configPath)
    str_client_credentials = localReadConfig.get_flask_sqlalchemy_setting('client_credentials')
    parent_id = localReadConfig.get_flask_sqlalchemy_setting('parent_id_folder')

    '''Delete all rows first.'''
    GDrive_MoneyHunter([],db,GoogleDrive_callputjpg).DB_DeleteAll()

    str_candlestick_filepath = ''#
    localgoogle_drive = GoogleCloudDrive(str_candlestick_filepath)
    gauth = localgoogle_drive.GDriveAuth(str_client_credentials)
    drive = GoogleDrive(gauth)

    list_foldersfiles=localgoogle_drive.listfolder(drive,parent_id)
    '''Then insert data into table.'''    
    #GDrive_MoneyHunter(list_foldersfiles,db).DB_Insert()
    GDrive_MoneyHunter(list_foldersfiles,db,GoogleDrive_callputjpg).DB_Insert()