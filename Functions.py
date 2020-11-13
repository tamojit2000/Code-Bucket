import pickle
import os

def Load_User_Database():
    try:
        f=open('User_Database.dat','rb')
        obj=pickle.load(f)
        f.close()
        return obj
    except:
        obj=dict()
        return obj

def Write_User_Database(USER_DATABASE,User):
    f=open('User_Database.dat','wb')
    USER_DATABASE[User.Username]=User
    pickle.dump(USER_DATABASE,f)
    f.close()


def Load_Question_Database():
    # data=[
    #     {
    #         'id':1,
    #         'statement':'Input and print factorial.',
    #         'explanation':'0!=1 1!=1 3!=6'
    #     },
    #     {
    #         'id':2,
    #         'statement':'Input and print Odd or Even.',
    #         'explanation':'0=Even 1=Odd'
    #     },
    #     {
    #         'id':3,
    #         'statement':'Input and print fibonacci.',
    #         'explanation':'1=1 2=1 3=2 4=3 5=5 6=8'
    #     }
    # ]

    data=[]
    for file in os.listdir('Questions'):
        f=open('Questions'+'\\'+file+'\\statement.txt','r')
        statement=f.read()
        f.close()
        d={'id':int(file),'explanation':statement}
        data.append(d)

    data=sorted(data,key=lambda x: x['id'])

    return data

def Prepare_rank_list(data_dict):
    l=[]
    for i in data_dict:
        l.append([data_dict[i].Score,data_dict[i].Username])
    l.sort(reverse=True)
    data=[]
    c=1
    for i in l:
        if data==[]:
            data.append([c,i[0],i[1]])
        else:
            if data[-1][1]==i[0]:
                data.append([c,i[0],i[1]])
            else:
                c+=1
                data.append([c,i[0],i[1]])
    return data

def Increase_views():
    value=0
    try:
        f=open('Views_Database.dat','rb')
        value=pickle.load(f)
        f.close()
    except:
        pass

    value+=1
    f=open('Views_Database.dat','wb')
    pickle.dump(obj=value,file=f)
    f.close()
    return value
