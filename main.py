from flask import Flask,render_template,request,redirect
from User import *
from Functions import *


USER_DATABASE=Load_User_Database()
QUESTION_DATABASE=Load_Question_Database()

app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main_page',methods=['POST','GET'])
def main_page():
    if request.method=='POST':
        Username=request.form['Username']
        Password=request.form['Password']

        if (Username in USER_DATABASE) and USER_DATABASE[Username].Password==Password:
            status='Ok'
            User=USER_DATABASE[Username]
        elif (Username in USER_DATABASE) and USER_DATABASE[Username].Password!=Password:
            status='Wrong'
            User=USER_DATABASE[Username]
        elif Username not in USER_DATABASE:
            status='New'
            User=User(Username,Password)
            Write_User_Database(USER_DATABASE,User)



        return render_template('main_page.html',User=User,Status=status,Question=QUESTION_DATABASE)
    else:
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
