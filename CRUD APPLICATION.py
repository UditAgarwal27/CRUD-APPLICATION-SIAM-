print("                 CRUD APPLICATION  FOR ACCESSING THE DATABASE   ")




import sqlite3


conn=sqlite3.connect('DATABASE.db')                 #### CREATING AND CONNECTING TO A DATABASE ####


c=conn.cursor()                                    #### CREATING A CURSOR FOR TRAVERSING THE DATABASE ####

#### CREATING A TABLE #### 

#c.execute("""CREATE TABLE task (                                           
#                               id integer PRIMARY KEY,                       
#                                task VARCHAR(255)                             
#                               )""")


#### AFTER EXECUTING THE MODULE ONCE DROP THE CREATION OF THE TABLE IN COMMENT SECTION BY USING #, OTHERWISE ERROR WILL COME SAYING, TABLE NAMED 'task' ALREADY EXIST####


#DEFINING THE FUNCTIONS#


#### FUNCTION FOR RECORDING A TASK WITH PARTICULAR ID ####
def insert(id,data):
    c.execute("INSERT INTO task VALUES (:id,:task)",{'id':id,'task':data})
    conn.commit()
    print("\nRecord inserted.\n")

####FUNCTION FOR VIEWING ALL THE TASK RECORDED ####
def view():
    e=0
    c.execute("SELECT * FROM task")
    while True:
        row=c.fetchone()
        if row==None:
            if(e==0):
                print("No record Inserted")
                break
            break
        print("\nAll the task recorded along with ID Number\n")
        print(row,"\n")
        e=e+1
    

#### FUCNTION FOR UPDATING THE RECORD (IF EXIST) ####
def update(id,task):
    c.execute(""" UPDATE task SET task=:task
                  WHERE id=:id""",
                  {'id':id, 'task':task})
    conn.commit()
    print("\n Record updated.\n")


#### FUNCTION FOR DELETING A RECORD (IF EXIST) ####
def delete(id):
    c.execute(""" DELETE from task WHERE id=:id""",
                  {'id':id})
    conn.commit()
    print("\n Record Deleted.\n")


#### FUNCTION FOR CHECKING WEATHER A RECORD WITH PARTICULAR ID EXIST  ####
def exist(id):
    d=0
    c.execute("SELECT * FROM task")
    while True:
        row=c.fetchone()

        if row==None:
            break
        if(row[0]==id):
            d=d+1
    return d
    
#MAIN MENU  (USER'S CHOICE)
print("1. ADD TASK")

print("2. VIEW TASK")

print("3. UPDATE TASK")

print("4. DELETE TASK\n")

print("Enter Choice")

choice=int(input())



#INITIAL CASES::::::

if choice==1:     
    print("\nEnter The unique ID")
    id=int(input())
    ans=exist(id)
    if ans==0:
        print("Enter the Task")
        data=input()
        insert(id,data)
    else:
        print("Record With Similar ID Exist , So Task cannot be recorded")

elif choice==2:
    view()

elif choice==3:
    print("enter the ID of Record of which you want to update the task")
    id=int(input())
    
    ans=exist(id);
    if ans==0:
        print("Record does not exist And Cannot be Updated")
    else:
        print("Enter the new task for the ID")
        task=input()
        update(id,task)

elif choice==4:
    print("Enter the ID of the Record to be deleted")
    id=int(input())
    ans=exist(id);
    if ans==0:
        print("Record does not exist And Cannot be Deleted\n")
    else:
        delete(id)


print("Do You Want To Continue y/n")        #### USER'S CHOICE TO CONTINUE ACCESSING THE DATABASE OR NOT####
ans=input()

if ans=='n':
    print("\nProcess Completed")
    
else:
    
    print("\n")
    while(ans=='y'):                        #### WHILE LOOP FOR CONTINOUSLY ACCESSING THE DATABSE DEPENDING ON USER'S CHOICE####
        print("1. ADD TASK")                     
                                          
        print("2. VIEW TASK")                 ####     SAME MENU      #### 

        print("3. UPDATE TASK")                   ####   FOR USERS CHOICE  ####

        print("4. DELETE TASK\n")

        print("enter choice")

        choice=int(input())

        if choice==1:
            print("\nEnter unique id")
            id=int(input())
            print("Enter the task")
            data=input()
            insert(id,data)

        elif choice==2:
            view()

        elif choice==3:
            print("enter the ID of which you want to update the task")
            id=int(input())
            ans=exist(id);
            if ans==0:
                print("Record does not exist And Cannot be Updated")
            else:
                print("Enter the new task for the ID")
                task=input()
                update(id,task)

        elif choice==4:
            print("Enter the ID of the record to be deleted")
            id=int(input())
            ans=exist(id);
            if ans==0:
                print("Record does not exist And Cannot be Deleted\n")
            else:
                delete(id)

        print("Do You Want To Continue y/n")        #### USER'S PERMISSION FOR ACCESSING THE DATABASE AGAIN??    ####
        ans=input()
        if ans=='n':
            print("Process Completed")
            break;
        else:
            continue

        
conn.commit()
conn.close()                                #### FOR SAVING CHANGES $####

