from flask import *
from datetime import datetime
from dbModel import *
from urllib.parse import urlparse

# 2018/11/14 
# https://stackoverflow.com/questions/45274152/flask-sqlalchemy-keyerror-sqlalchemy-track-modifications?rq=1
#app = Flask(__name__)

app.debug=True

@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    #data_GoogleDrive_callputjpg = GoogleDrive_callputjpg.query.all()
    #2018/11/30 select 50 row records for testing
    data_GoogleDrive_callputjpg = GoogleDrive_callputjpg.query.filter(GoogleDrive_callputjpg.Id.between('1', '100'))
    history_dic = {}
    history_list = []
    for _data in data_GoogleDrive_callputjpg:
        history_dic['title'] = _data.title
        history_dic['Id'] = _data.Id
        #2018/11/29
        #https://stackoverflow.com/questions/38490651/how-to-displayimage-from-google-drive-at-page-html
        # Replace the open part of the link with uc and it will work. It will become 
        # <img src="https://drive.google.com/uc?id=0B0etQtBsI2KmVGVmYjNOSS15VVk" />
        '''
        >>from urllib.parse import urlparse
        >>url="https://drive.google.com/file/d/1jprj0v8z6sf_traLnXIIGgOnFJkB7_UN/view?usp=drivesdk"
        >>> parsed = urlparse(url)
        >>>print(parsed)
        ParseResult(scheme='https', netloc='drive.google.com', path='/file/d/1jprj0v8z6sf_traLnXIIGgOnFJkB7_UN/view', params='', query='usp=drivesdk', fragment='')
        >>> print(parsed.path.split('/'))
        ['', 'file', 'd', '1jprj0v8z6sf_traLnXIIGgOnFJkB7_UN', 'view']
        '''
        gdrive_fileid = urlparse(_data.title1).path.split('/')[-2]
        history_dic['gdrive_fileid'] = '{}'.format(gdrive_fileid)
        #history_dic['title1'] = "<img src=\"https://drive.google.com/uc?id={}\" alt=\"\" />".format(gdrive_fileid)#_data.title1
        #history_dic['title1'] = "https://drive.google.com/uc?id={}".format(gdrive_fileid)
        ''''
        https://support.awesome-table.com/hc/en-us/articles/115002196665-Display-images-from-Google-Drive
        3 - Display your images
        Now that we have the image IDs and we've properly configured the sharing settings, we can specify how the images should be displayed using the prescribed formats below.
        
        Since we're using templates, this means we can also specify the dimensions:
        https://drive.google.com/thumbnail?id={{imageID}}&sz=w{{width}}-h{{height}}
        You can use absolute values (pixels) or relative values (%) when specifying the width and height.
        '''
        history_dic['title1'] = "https://drive.google.com/thumbnail?id={}&sz=w950-h800".format(gdrive_fileid)

        history_dic['modifiedDate'] = _data.modifiedDate#.strftime('%Y/%m/%d %H:%M:%S')
        history_list.append(history_dic)
        history_dic = {}
    return render_template('index.html', **locals())


@app.route('/API/add_data', methods=['POST'])
def add_data():
    name = request.form['name']
    description = request.form['description']
    if name != "" and description != "":
        add_data = UserData(
            Name=name,
            Description=description,
            CreateDate=datetime.now()
        )
        db.session.add(add_data)
        db.session.commit()
    return redirect('index')


if __name__ == '__main__':
    app.run(debug=True)
