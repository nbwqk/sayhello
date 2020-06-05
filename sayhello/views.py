from flask import flash,redirect,url_for,render_template

from . import app,db
from .models import Message
from .forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    messages=Message.query.order_by(Message.timestamp.desc()).all() # 按时间戳降序取出所有记录
    form=HelloForm()
    if form.validate_on_submit():
        name=form.name.data
        body=form.body.data
        message=Message(body=body,name=name) # 实例化模型，创建记录
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html',form=form,messages=messages)