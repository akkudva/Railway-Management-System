from tkinter import *
from tkinter import messagebox as mb 
from id_generator import *

win=Tk()
win.geometry("500x500")
win.title("railway management")

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root", passwd="", database='railway')

myc=mydb.cursor()
myu=mydb.cursor()
mye=mydb.cursor()

#GUI CODE STARTS HERE

win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)

global e11, e12, l14, l53, switch_frame


def switch_frame(fr):
    fr.tkraise()

def clear_entry(e1, e2):
    e1.delete(0, END)
    e2.delete(0, END)

def del_lab(l1):
      l1.after(1000 , lambda: l1.destroy())

global u_name


#login page-----------------------------------------------------------------------

f1=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

def get_val():
    global u_name
    u_name=e11.get()
    p_wd=e12.get()
    
    if(u_name=="" or p_wd==""):
        pass
    else:
      query=("select * from user where username=%s")
      data=(u_name,)
      myu.execute(query, data)
      myu.fetchall()
      if(myu.rowcount==0):
          global l14
          l14=Label(f1, text="you are not a user", font="arial 10", fg="red")         
          l14.place(x=500, y=300) 
      else:
         switch_frame(f3)
         clear_entry(e11, e12)    



l11=Label(f1, text="Enter username", font="arial 15", fg="red")
l11.place(x=200, y=200)

l12=Label(f1, text="Enter password", font="arial 15", fg="red")
l12.place(x=200, y=300)

b11=Button(f1, text="Login", command=lambda:get_val(), width=20, height=2)
b11.place(x=200, y=400)

b12=Button(f1, text="Create new username", command=lambda:[switch_frame(f2), del_lab(l14), clear_entry(e11, e12)], width=20, height=2)
b12.place(x=500, y=400)

e11=Entry(f1, width=40)
e11.place(x=600, y=200)

e12=Entry(f1, show="*", width=40)
e12.place(x=600, y=300)



# --------------------------------------------------------------------------------

# create username page

f2=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

global e21, e22

def get_value():
    u_name=e21.get()
    p_wd=e22.get()
    query=("Insert into USER(username, password)" " values(%s, %s)")
    data=(u_name, p_wd)
    myc.execute(query, data)
    clear_entry(e21, e22)
    
l21=Label(f2, text="Enter new username", font="arial 20", fg="red")
l21.place(x=200, y=200)

l22=Label(f2, text="Enter password", font="arial 20", fg="red")
l22.place(x=200, y=300)

b21=Button(f2, text="Create", command=lambda:[switch_frame(f1), get_value()], width=20, height=2)
b21.place(x=200, y=400)

b22=Button(f2, text="Back", command=lambda:switch_frame(f1), width=20, height=2)
b22.place(x=500, y=400)

e21=Entry(f2)
e21.place(x=600, y=200)

e22=Entry(f2, show="*")
e22.place(x=600, y=300)

#--------------------------------------------------------------------------------------
#book cancel check page
f3=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

b31=Button(f3, text="Book Ticket",  command=lambda:[switch_frame(f4)], width=20, height=2)
b31.place(x=500, y=200)

b32=Button(f3, text="Cancel Ticket",  command=lambda:[switch_frame(f5)], width=20, height=2)
b32.place(x=500, y=300)

b33=Button(f3, text="Check Ticket",  command=lambda:[switch_frame(f6)], width=20, height=2)
b33.place(x=500, y=400)

b34=Button(f3, text="Back", command=lambda:[switch_frame(f1)], width=20, height=2)
b34.place(x=500, y=500)


#book page
f4=Frame(win,height=500, width=500, cursor="arrow", bg='gray')
global e41, e42

l41=Label(f4, text="From : ", font="arial 20", fg="red")
l41.place(x=400, y=100)

l42=Label(f4, text="To: ", font="arial 20", fg="red")
l42.place(x=400, y=200)

b41=Button(f4, text="Search",  command=lambda:[switch_frame(f7),get_train()], width=20, height=2)
b41.place(x=500, y=400)

b42=Button(f4, text="Back",  command=lambda:[switch_frame(f3), clear_entry(e41, e42)], width=20, height=2)
b42.place(x=200, y=400)

e41=Entry(f4)
e41.place(x=500, y=100)

e42=Entry(f4)
e42.place(x=500, y=200)

#cancel page
f5=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

l51=Label(f5, text="Passenger ID:", font="arial 20", fg="red")
l51.place(x=200, y=100)


l52=Label(f5, text="Ticket ID:", font="arial 20", fg="red")
l52.place(x=200, y=200)


b52=Button(f5, text="Back", width=20, height=2, command=lambda:[switch_frame(f3),del_lab(l53)])
b52.place(x=400, y=500)

global e51, e52, e53
e51=Entry(f5)
e51.place(x=400, y=100)

e52=Entry(f5)
e52.place(x=400, y=200)



def cancel():
    global l53
    l53=Label(f5, text="Ticket cancelled", fg="red", font="arial 15")
    l53.place(x=500, y=500)

def del_cont():
     p_id=e51.get()
     t_id=e52.get()
     query1=("Delete from PASSANGER where passenger_id=%s")
     data1=(p_id,)
     myc.execute(query1,data1)
     
     query2=("Delete from TICKET where ticket_id=%s")
     data2=(t_id,)
     myc.execute(query2, data2)

     

b51=Button(f5, text="Cancel Ticket", command=lambda:[cancel(), del_cont(), clear_entry(e51, e52), clear_entry(e52, e53)], width=20, height=2)
b51.place(x=200, y=500)

#check page
f6=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

l61=Label(f6, text="Passenger ID:", font="arial 20", fg="red")
l61.place(x=200, y=300)

l62=Label(f6, text="Ticket ID:", font="arial 20", fg="red")
l62.place(x=200, y=400)

b61=Button(f6, text="Check", width=10, command=lambda:[switch_frame(f9), display_tick()])
b61.place(x=250, y=500)

b62=Button(f6, text="Back", width=10, command=lambda:[switch_frame(f3), clear_entry(e61, e62)])
b62.place(x=400, y=500)

e61=Entry(f6)
e61.place(x=450, y=300)

e62=Entry(f6)
e62.place(x=450, y=400)
# ------------------------------------------------------------------------------------------------------------
# CHECK AVAILABLE TRAINS
f7=Frame(win,height=500, width=500, cursor="arrow", bg='gray')
global l, l71


def get_train():
      global l, l72
      l72=Label(f7, text="Train Name | Train No | Date |", font="arial 17")
      l72.place(x=50, y=10)
      st=e41.get()
      so=e42.get()
      data=(st, so)
      query=("select t.train_name, t.train_No, t.departure_date from train t where t.starts_at=%s and stops_at=%s")
      myc.execute(query, data)   
      r=myc.fetchall()
      if(myc.rowcount==0):
            switch_frame(f4)
         
      h=50
      v=50
      for i in r:
        l=Label(f7, text=i, font="arial 18")
        l.place(x=h, y=v)
        v=v+10  
      if(myc.rowcount==0):
        {
            switch_frame(f4)
        }
         
    
l71=Label(f7, text="Train Number: ", font="arial 20", fg="red")
l71.place(x=200, y=250)


b71=Button(f7, text="Book", width=20, height=2 ,command=lambda:[switch_frame(f8)])
b71.place(x=300, y=400)

b72=Button(f7, text="Back", width=20, height=2, command=lambda:[switch_frame(f4), del_lab(l), clear_entry(e71, e72)])
b72.place(x=100, y=400)

e71=Entry(f7)
e71.place(x=450, y=250)

e72=Entry(f7)
e72.place(x=4000, y=500)

#------------------------------------------------------------------------------------------
#BOOK TICKET
f8=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

def con_tick():
    p_fname=e81.get()
    p_lname=e84.get()
    gen=e82.get()
    a=e83.get()
    tick_id=gen_tick()
    tick_stat="booked"
    pass_id=gen_pass()
    tr_no=e71.get()
    fr_st=e41.get()
    to_st=e42.get()
    global l85
    l85=Label(f8, text="Passenger_id= "+pass_id+": Ticket_id="+tick_id, font="arial 15", fg="red")
    l85.place(x=600, y=600)
    if p_fname or gen or a or p_lname =="":
        pass
    data1=(tick_id, tick_stat, tr_no, pass_id, fr_st, to_st)
    query1="Insert into TICKET (Ticket_id, Ticket_status, Train_No, Passenger_id, From_Station, To_Station) VALUES(%s, %s, %s, %s, %s, %s)"
    myc.execute(query1, data1)
    mydb.commit()
    
    

    query3="Insert into PASSANGER(First_Name, Last_Name, Age, Gender, Passenger_id, username) values(%s, %s, %s, %s, %s, %s)"
    data3=(p_fname, p_lname, a, gen, pass_id, u_name)
    myc.execute(query3, data3)
    
global l85

l81=Label(f8, text="Passenger First Name: ", font="arial 20", fg="red")
l81.place(x=200, y=100)

l84=Label(f8, text="Passanger Last Name: ", font="Arial 20", fg="red")
l84.place(x=200, y=200)

l82=Label(f8, text="Gender: ", font="arial 20", fg="red")
l82.place(x=200, y=300)
 
l83=Label(f8, text="Age: " , font="arial 10", fg="red")
l83.place(x=200, y=400)

b81=Button(f8, text="Confirm", width=20, height=2, command=lambda:[con_tick(),clear_entry(e81, e82), clear_entry(e83, e84), del_lab(l), del_lab(l72)])
b81.place(x=400, y=500)

b82=Button(f8, text="Back", width=20, height=2, command=lambda:[switch_frame(f7), del_lab(l85)])
b82.place(x=100, y=500)

e81=Entry(f8)
e81.place(x=500, y=100)

e84=Entry(f8)
e84.place(x=500, y=200)

e82=Entry(f8)
e82.place(x=500, y=300)

e83=Entry(f8)
e83.place(x=500, y=400)

   
#-------------------------------------------------------------------------------------------
f9=Frame(win,height=500, width=500, cursor="arrow", bg='gray')

global l91
def display_tick():
    p_id=e61.get()
    t_id=e62.get()
    l90=Label(f9, text="Ticket_id | Ticket_Status | Passenger_id |", font="Arial 15")
    l90.place(x=150,y=10)
    global l91
    if(p_id or t_id ==""):
        pass
    
    data1=(t_id, p_id)
    query1=("select t.Ticket_id, t.Ticket_status, p.passenger_id  from Ticket t, PASSANGER p where t.passenger_id=p.passenger_id and t.ticket_id=%s and p.passenger_id=%s")
    myc.execute(query1, data1)
    r=myc.fetchall()
    h=25
    v=20
    for i in r:
          l91=Label(f9, text=i, font="arial 18")
          l91.place(x=150, y=50)
          v=v+10   

b91=Button(f9, text="Back", width=10, command=lambda:[del_lab(l91), switch_frame(f6), clear_entry(e61, e62)])
b91.place(x=100, y=200)

for f in (f1, f2, f3, f4, f5, f6, f7, f8, f9):
     f.grid(row=0, column=0, sticky='nsew')
     f.columnconfigure(0, weight=1)
     f.rowconfigure(1, weight=1)
switch_frame(f1)

win.mainloop()

#GUI CODE ENDS HERE
