from django.shortcuts import render,redirect
import mysql.connector as mysql
import datetime

def index(req):
    return render(req,'index.html')

def userreg(req):
    return render(req,'userreg.html')

def regTask(req):
    if req.POST.get('user')=="user":
        name=req.POST.get('name')
        fname=req.POST.get('fname')
        mobile=req.POST.get('mob')
        email=req.POST.get('email')
        password=req.POST.get('pass')
        gender=req.POST.get('gender')
        con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
        cr=con.cursor()
        sql="insert into user(name,fname,mobile,email,password,gender) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(name,fname,mobile,email,password,gender);
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect('/userlogin')
    else:
        name=req.POST.get('name')
        fname=req.POST.get('fname')
        mobile=req.POST.get('mob')
        email=req.POST.get('email')
        password=req.POST.get('pass')
        gender=req.POST.get('gender')
        con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
        cr=con.cursor()
        sql="insert into employee(name,fname,mobile,email,password,gender) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(name,fname,mobile,email,password,gender);
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect('/userlogin')

def userlogin(req):
    return render(req,'userlogin.html')

def adminlogin(req):
    return render(req,'adminlogin.html')

def loginTask(req):
    if req.POST.get('admin')=="user":
        email=req.POST.get('email')
        password=req.POST.get('pass')
        con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
        cr=con.cursor()
        sql="select * from user where email='{0}' and password='{1}'".format(email,password);
        cr.execute(sql)
        rec=cr.fetchall()
        global rec2
        rec2=rec
        if rec==[]:
            return redirect('/userlogin')
        else:
            global email2
            email2=email
            global pass1
            pass1=password
            return redirect('/productlogin')
    
    elif req.POST.get('admin')=="admin":
        email="admin@gmail.com"
        password="admin123"
        adminemail=req.POST.get('email')
        adminpass=req.POST.get('pass')
        if email==adminemail and password==adminpass:
            return redirect('/adminprofile')
        
        else:
            return redirect('/userlogin')
    else:
        return redirect('/userlogin')



def adminprofile(req):
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1") 
    cr=con.cursor()
    sql="select count(id) from user";
    cr.execute(sql)
    rec=cr.fetchall()

    ssql="select count(id) from products";
    cr.execute(ssql)
    rec1=cr.fetchall()

    tsql="select sum(Amount) from history";
    cr.execute(tsql)
    rec2=cr.fetchall()

    fsql="select sum(quantity) from history";
    cr.execute(fsql)
    rec3=cr.fetchall()

    fisql="select count(id) from history";
    cr.execute(fisql)
    rec4=cr.fetchall()

    return render(req,'adminprofile.html',{'rec':rec,'rec1':rec1,'rec2':rec2,'rec3':rec3,'rec4':rec4})

def productshow(req):
    return render(req,'productshow.html')

def productlogin(req):
    return render(req,'productlogin.html')

def buy(req):
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="select * from products";
    cr.execute(sql)
    rec=cr.fetchall()
    return render(req,'buy.html',{'rec':rec})

def userprofile(req):
    h=rec2
    return render(req,'userprofile.html',{'h':h})

def ulogout(req):
    return render(req,'ulogout.html')

def cart(req):
    return render(req,'cart.html')

def addproduct(req):
    return render(req,'addproduct.html')

def cartdesk(req):
    sid=req.GET.get('sid')
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="select id,P_name,Brand,Amount from products where id={0}".format(sid)
    cr.execute(sql)
    rec=cr.fetchall()
    return render(req,'cartdesk.html',{'rec':rec})

def buyTask(req):
    bid=req.GET.get('bid')
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="select * from products where id={0}".format(bid)
    cr.execute(sql)
    rec=cr.fetchall()
    return render(req,'buyTask.html',{'rec':rec})

def buyTaskdone(req):
    pname=req.POST.get('pname')
    bname=req.POST.get('bname')
    amount=req.POST.get('am')
    available=req.POST.get('avai')
    quantity=req.POST.get('qua')
    
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="insert into history(P_name,Brand,Amount,Available,quantity) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(pname,bname,amount,available,quantity);
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect('/history')

def history(req):
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="select * from history";
    cr.execute(sql)
    rec=cr.fetchall()
    return render(req,'history.html',{'rec':rec})

def adminhistory(req):
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="select * from history";
    cr.execute(sql)
    rec=cr.fetchall()

    sql1="select name,email from user";
    cr.execute(sql1)
    rec1=cr.fetchall()
    return render(req,'adminhistory.html',{'rec':rec,'rec1':rec1})

def addproductTask(req):
    pname=req.POST.get('pname')
    bname=req.POST.get('bname')
    amount=req.POST.get('am')
    available=req.POST.get('avai')
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="insert into products(P_name,Brand,Amount,Available) values('{0}','{1}','{2}','{3}')".format(pname,bname,amount,available);
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect('/addproduct')

def delete(req):
    sid=req.GET.get('sid')
    con=mysql.connect(host="localhost",user="root",passwd="dp089901",database="django1")
    cr=con.cursor()
    sql="delete from history where id={0}".format(sid)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect('/adminhistory')

def useradmindata(req):
    return render(req,'useradmindata.html')




    
    
