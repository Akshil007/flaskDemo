from flask import Flask,render_template,url_for,redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akshil99@localhost/test'
db = SQLAlchemy(app)
data = []

class form(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(30))
    mobileNo = db.Column(db.String(30))
    address = db.Column(db.String(30))

    def __repr__(self):
        return '<From %r>' % self.id

@app.route('/',methods=['POST','GET'])
def index():
    data = form.query.all()
    return render_template("index.html", data=data)

@app.route('/add',methods=['POST','GET'])
def addData():
    if request.method=='POST':
        name = request.form.get("name")
        mobileNo = request.form.get("mob")
        address = request.form.get("adr")
        new_user = form(name=name,mobileNo=mobileNo,address=address)
        # return ("data"+str(name)+str(mobileNo)+str(address))

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return 'something went wrong!!!'
    else:
        return redirect('/')  

@app.route('/delete/<int:id>')
def deleteData(id):
    data_to_delete = form.query.get_or_404(id)

    try:
        db.session.delete(data_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        # return redirect('/')
        return "something went wrong!!!"


@app.route('/update/<int:id>', methods=['POST','GET'])
def updateData(id):
    data_to_update = form.query.get_or_404(id)
    if(request.method=='POST'):
        try:
            #db.session.update(data_to_update)
            db.session.delete(data_to_update)

            name = request.form.get("name")
            mobileNo = request.form.get("mob")
            address = request.form.get("adr")
            new_user = form(name=name,mobileNo=mobileNo,address=address)

            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return "Something went wrong!!!"
    else:
        return render_template("update.html", data=data_to_update)


if(__name__ == "__main__"):
    app.run(debug = True)
    

