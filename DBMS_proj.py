import mysql.connector
from mysql.connector import Error
import numpy as np
import matplotlib.pyplot as plt
import math

def onepass():
    inp="";
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='digifam',
                                         user='root',
                                         password='Banger2170@3')
        cursor = connection.cursor()
        if (connection.is_connected()):
            try:
                inp = input("enter user id :");
                option = 0;
                while (option!=9):
                    print("choose an option \n 1) view user details\n 2) view events hosted by you\n 3) view your subscription details\n 4) view your medical history\n 5) view your insurance details\n 6) view your school history\n 7) view your family graph\n 8) corona people in your relation \n 9) exit");
                    option = int(input());
                    if option==1:
                        mysql_query = f"""SELECT * FROM user_data where Person_id ='{inp}'""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)

                    elif option==2:
                        mysql_query = f"""SELECT * FROM event where Organiser_id ='{inp}'""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==3:
                        mysql_query = f"""SELECT * FROM subscription where Person_id ='{inp}'""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==4:
                        mysql_query = f"""SELECT * FROM medical_sercives where Person_id ='{inp}'""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==5:
                        mysql_query = f"""SELECT * FROM insurance where Person_id ='{inp}'""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==6:
                        mysql_query = f"""SELECT * FROM school where person_id ='{inp}'""";
                        cursor = connection.cursor()
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==7:
                        mysql_query = f"""SELECT R.priority,U.name FROM relation R, user_data as U where user_1_id ='{inp}' AND R.user_2_id = U.Person_id""";
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        arr1=[[],[],[]]
                        for row in result:
                            print(row)
                            
                            if(int(row[0])<=2):
                                arr1[2].append(row[1])
                            elif ( int(row[0])<=6):
                                arr1[1].append(row[1])
                            else:
                                arr1[0].append(row[1])
                        fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"),figsize = (20,20))
                        ax.axis("off")

                        plot(ax,[1]*len(arr1[0]),[2]*len(arr1[1]),[3]*len(arr1[2]),arr1[0],arr1[1],arr1[2])
                        ax.relim()
                        ax.autoscale()
                        print(ax.get_xlim(),ax.get_ylim())
                        plt.show()

                    elif option==8:
                        mysql_query = f"""SELECT U.name FROM medical_sercives as M, user_data as U, relation R where R.user_1_id ='{inp}' AND U.person_id = M.patient_ID AND U.person_id = R.user_2_id and M.Disease ="corona" """;
                        cursor.execute(mysql_query);
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                    elif option==9:
                        print("going back to main menu")
                    else:
                        print("invalid input , try again!!")
            except ValueError:
                print("sorry query can't be executed, returning to main menu")
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def plot(ax,r1,r2,r3,name1,name2,name3):

    color = ["pink", "palegreen", "paleturquoise" ]

    circ = plt.Circle((0,0), 30, edgecolor = "black", facecolor = "none")
    ax.add_patch(circ)

    circ = plt.Circle((0,0), 50, edgecolor = "black", facecolor = "none")
    ax.add_patch(circ)

    circ = plt.Circle((0,0), 70, edgecolor = "black", facecolor = "none")
    ax.add_patch(circ)

    circ = plt.Circle((0,0), 15, color = "thistle")
    ax.add_patch(circ)
    label = ax.annotate("you", xy=(0,0), fontsize= 8, ha="center")





    for i in range(len(r3)):
        name3[i] = name3[i].replace(" ","\n")
        coord = (30*math.cos((i+1)*2*math.pi/len(r3)), 30*math.sin((i+1)*2*math.pi/len(r3)))        
        circ = plt.Circle(coord, 10, color = color[0])
        ax.add_patch(circ)
        label = ax.annotate(name3[i], xy=coord, fontsize=8, ha="center",va ="center")

    for i in range(len(r2)):
        name2[i] = name2[i].replace(" ","\n")
        coord = (50*math.cos((i+1)*2*math.pi/len(r2)),50*math.sin((i+1)*2*math.pi/len(r2)))         
        circ = plt.Circle(coord, 10, color = color[1])
        ax.add_patch(circ)
        label = ax.annotate(name2[i], xy=coord, fontsize=8, ha="center",va ="center")

    for i in range(len(r1)):
        name1[i] = name1[i].replace(" ","\n")
        coord = (70*math.cos((i+1)*2*math.pi/len(r1)), 70*math.sin((i+1)*2*math.pi/len(r1)))        
        circ = plt.Circle(coord, 10, color = color[2])
        ax.add_patch(circ)
        label = ax.annotate(name1[i], xy=coord, fontsize=8, ha="center",va ="center")

def thirdpass():
    sq_q ="";
    while(sq_q!="exit"):
        sq_q = input();
        if sq_q!= "exit":
            try:
                connection = mysql.connector.connect(host='localhost',
                                                 database='digifam',
                                                 user='root',
                                                 password='Banger2170@3')
                cursor = connection.cursor()
                if (connection.is_connected()):
                    cursor.execute(sq_q);
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
            except Error as e:
                print("Error while connecting to MySQL", e)
        
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
                    sq_q ="exit"
onepass();
thirdpass();
