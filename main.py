from flask import Flask,render_template,request,redirect
from User import *
from Functions import *




app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main_page',methods=['POST','GET'])
def main_page():
    if request.method=='POST':
        Username=request.form['Username']
        Password=request.form['Password']

        USER_DATABASE=Load_User_Database()
        QUESTION_DATABASE=Load_Question_Database()

        if (Username in USER_DATABASE) and USER_DATABASE[Username].Password==Password:
            status='Ok'
            user=USER_DATABASE[Username]
        elif (Username in USER_DATABASE) and USER_DATABASE[Username].Password!=Password:
            status='Wrong'
            user=USER_DATABASE[Username]
        elif Username not in USER_DATABASE:
            status='New'
            user=User(Username,Password)
            Write_User_Database(USER_DATABASE,user)



        return render_template('main_page.html',User=user,Status=status,Question=QUESTION_DATABASE)
    else:
        return redirect('/')

@app.route('/check',methods=['POST','GET'])
def check():
    if request.method=='POST':
        file=request.files['file']
        index=request.form['index']
        file.save(file.filename)

        f=open(file.filename,'r')
        data=f.read()
        f.close()

        return render_template('check.html',Data=data,Index=index)
    else:
        return  redirect('/')


if __name__=='__main__':
    app.run(debug=True)
