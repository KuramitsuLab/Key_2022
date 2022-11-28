from flask import Flask
from flask import render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#アプリケーション作成
app = Flask(__name__) #アプリケーションのインスタンス化・実体化

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///key.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)#自動生成
    age = db.Column(db.String(30), nullable=False)
    job = db.Column(db.String(30), nullable=False)
    job_d = db.Column(db.String(30), nullable=True)
    exp = db.Column(db.String(30), nullable=False)
    confi = db.Column(db.String(30), nullable=False)
    lang = db.Column(db.String(30), nullable=True)

    # quest_form = db.Column(db.String(30), nullable=True)



@app.route("/", methods=['GET', 'POST'])
def quest():
    if request.method == 'POST':

        id = request.form.get('id')
        age = request.form.get('age')
        job = request.form.get('job')
        job_d = request.form.get('job_d')
        exp = request.form.get('exp')
        confi = request.form.get('confi')
        lang = request.form.get('lang')

        # quest_form = request.form.get('quest_form')

        post = Post(id=id,age=age,job=job,job_d=job_d,exp=exp,confi=confi,lang=lang)
        # post = Post(quest_form=quest_form)

        db.session.add(post)
        db.session.commit()  #保存
        print(post.job)

        return redirect('/quest.html')
    else:
        return render_template('/quest.html')
        



@app.route("/logger",methods=['GET', 'POST'])
def logger():
    return render_template('logger.html')

#習熟度の分類結果の表示ページを新しく作るか迷い中
@app.route('/result',methods=['GET', 'POST'])
def result():
    return render_template('result.html')


