import pickle
import os

def Load_User_Database():
    try:
        f=open(os.getcwd()+'User_Database.dat','rb')
        obj=pickle.load(f)
        f.close()
        return obj
    except:
        obj=dict()
        return obj

def Write_User_Database(USER_DATABASE,User):
    f=open(os.getcwd()+'User_Database.dat','wb')
    USER_DATABASE[User.Username]=User
    pickle.dump(USER_DATABASE,f)
    f.close()


def Load_Question_Database():
    data=[
        {
            'id':1,
            'statement':'Input and print factorial.',
            'explanation':'0!=1 1!=1 3!=6'
        },
        {
            'id':2,
            'statement':'Input and print Odd or Even.',
            'explanation':'0=Even 1=Odd'
        },
        {
            'id':3,
            'statement':'Input and print fibonacci.',
            'explanation':'1=1 2=1 3=2 4=3 5=5 6=8'
        }
    ]

    return data
