# Please Use IDLE to run this if VS code does not support mysql
import datetime
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='1234', database='f_fire')
if conn.is_connected():
    print("Ready For Forest Fire Prediction")
else:
    print("check mysql python connection....")
cur=conn.cursor()

def entry():
    try:
        oxygen = int(input("Enter Oxygen Level(Out Of 100): "))
        temperature = int(input("Enter Temperature: "))
        humidity = int(input("Enter Humidity Level (Out of 100): "))
        fireoccure = int(input("Probability of Forest Fire(0/1): "))
        cur.execute("use f_fire")
        cur.execute("insert into fire values('{}','{}','{}','{}')".format(oxygen,temperature,humidity,fireoccure))
        conn.commit()
        print("Data Added Successfully")
    except Exception as  e:
        print("DATABASE ERROR:\t ",e)
        
#----------------------------------------------------------------------------------------------------------------

def predict():
    try:
        oxygen = int(input("Enter the Present Oxygen Level: "))
        temperature = int(input("Enter the Present Temperature: "))
        humidity = int(input("Enter the  Present Humidity Level: "))
        cur.execute("use f_fire")
        cur.execute("select * from fire")
        records=cur.fetchall()
        #print("Total number of rows in table: ", cur.rowcount)
        for row in records:
            if (row[0]== oxygen and row[1] == temperature and row[2]== humidity):
                if (row[3]== 1):
                    print("🔥Caution!🔥Chance of Forest Fire🔥🔥 ")
                else:
                    print("Very LOW chance of Forest Fire Today")
    except Exception as  e:
        print("database error",e)
        
        
#---------------------------------------------------------------------------------------------------------
while True:
    print("*"*80)
    print(" \t\t 🔥🔥🔥🔥 Forest Fire🔥🔥🔥🔥")
    print("\t")
    
    print("\t\t 1.☞ For New data Entries in Database  ")
    print("\t\t 2.☞ To Predict the Forest Fire ")
    print("\t\t 3.☞ To Exit Database ")
    
    print("*"*80)
    ch=int(input("Input Your Choice:"))
    print("*"*80)
    if ch==1:
        entry()
    elif ch==2:
        predict()
    elif ch==3:
        break
    else :
        print("Please Provide Valid Input.....")
