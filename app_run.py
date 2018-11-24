from flask import *
from datetime import datetime
from dbModel import *


# 2018/11/14 
# https://stackoverflow.com/questions/45274152/flask-sqlalchemy-keyerror-sqlalchemy-track-modifications?rq=1
#app = Flask(__name__)

app.debug=True

@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    data_GoogleDrive_callputjpg = GoogleDrive_callputjpg.query.all()
    history_dic = {}
    history_list = []
    for _data in data_GoogleDrive_callputjpg:
        history_dic['title'] = _data.title
        history_dic['Id'] = _data.Id
        history_dic['title1'] = _data.title1
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
