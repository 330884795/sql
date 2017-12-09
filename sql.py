from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = "tttwweewew"

class Name(Form):
    name = StringField('账号',validators=[Required()])
    submit = SubmitField('提交')




@app.route('/')
def hello_world():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/login',methods=['GET','POST'])
def login():
    name = None
    form = Name()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html',form=form,name=name)


@app.route('/search/<name>')
def echo(name):
    return render_template('search.html',name=name)

@app.route('/search/<int:number>')
def num(number):
    return render_template('search.html',number=number)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    manager.run()
