import mysql.connector
from mysql.connector import Error
import pickle
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import math

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


def onepass(cursor):
    inp="";
    try:
        inp = input("Enter user id: ");
        option = 0;
        while (option!=9):
            print("Choose an option \n1)View user details\n2)View events hosted by you\n3)View your subscription details\n4)View your medical history\n5)View your insurance details\n6)View your school history\n7)View your family graph\n8)Corona people in your relation \n9)Exit");
            option = int(input());
            if option==1:
                mysql_query = f"""SELECT * FROM user_data where Person_id ='{inp}'""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")   
            elif option==2:
                mysql_query = f"""SELECT * FROM event where Organiser_id ='{inp}'""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")    
            elif option==3:
                mysql_query = f"""SELECT * FROM subscription where Person_id ='{inp}'""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")    
            elif option==4:
                mysql_query = f"""SELECT * FROM medical_sercives where Person_id ='{inp}'""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")    
            elif option==5:
                mysql_query = f"""SELECT * FROM insurance where Person_id ='{inp}'""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")
            elif option==6:
                mysql_query = f"""SELECT * FROM school where person_id ='{inp}'""";
                cursor = connection.cursor()
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")
            elif option==7:
                mysql_query = f"""SELECT R.priority,U.name FROM relation R, user_data as U where user_1_id ='{inp}' AND R.user_2_id = U.Person_id""";
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                arr1=[[],[],[]]
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")
                for row in result:                    
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
                # print(ax.get_xlim(),ax.get_ylim())
                plt.show()

            elif option==8:
                mysql_query = f"""SELECT U.name FROM medical_sercives as M, user_data as U, relation R where R.user_1_id ='{inp}' AND U.person_id = M.patient_ID AND U.person_id = R.user_2_id and M.Disease ="corona" """;
                cursor.execute(mysql_query);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])
                print(tabulate(result, headers = column_list), end = "\n\n")

            elif option==9:
                print("Exiting")
            else:
                print("invalid input , try again!!")
    except ValueError:
        print("sorry query can't be executed, returning to main menu")
 

def second_type_query(cursor):

    f = open('helper.pkl', 'rb')
    dict1 = pickle.load(f)
    f.close()

    query = """show tables"""
    cursor.execute(query);
    result = cursor.fetchall()
    
    print('Tables:', end = '\n\n')
    for i in range(len(result)):
        print(str(i+1) + '. ' + result[i][0])
    
    while True:
        try:
            ch = int(input('\nSelect a table: '))
            if ch < 1 or ch > len(result):
                raise  exception
            break
        except:
            print('Enter a valid choice')

    table = result[ch-1][0]
    
    query = f"""select column_name from information_schema.columns where table_name = '{table}'"""
    cursor.execute(query);
    result = cursor.fetchall()

    column_list = []

    print('\nColumns:\n')
    for i in range(len(result)):
        print(str(i+1) + '. ' + result[i][0])
        column_list.append(result[i][0])

    print(str(i+2) + '. ' + 'All')

    n = i + 2

    b = []
    while True:
        try:
            print('\nSelect columns to print ( Enter space separated list of numbers)')
            a = [int(i) for i in input().split()]
            s = set()
            for c in a:
                s.add(c)
            for c in s:
                if c < 1 or c > n:
                    raise exception
                b.append(c)
            break

        except:
            print('Enter a valid list')

    if n in b:
        b = list(range(1, n))
    else:
        b.sort()

    b1 = []

    for i in b:
        b1.append(column_list[i-1])

    print('\nColumns:\n')
    for i in range(len(result)):
        print(str(i+1) + '. ' + result[i][0])

    c = []
    while True:
        try:
            print('\nSelect columns to filter rows ( Enter space separated list of numbers)')
            a = [int(i) for i in input().split()]
            s = set()
            for d in a:
                s.add(d)
            for d in s:
                if d < 1 or d > n-1:
                    raise exception
                c.append(d)
            break

        except:
            print('Enter a valid list')

    c.sort()

    query = f"""select {",".join(b1)} from {table} where """

    p = []
    for i in c:
        val = dict1[table][column_list[i-1]]
        l = []
        r = 0
        print("\nSelect the way of filtering by attribute '" + str(column_list[i-1]) + "'", end = '\n\n')

        if val != -1:
            r += 1
            print(str(r) + '. Get rows with exactly matching attributes value you enter')
        
        if val == 1 or val == 3:
            r += 1    
            print(str(r) + '. Enter a range\n')

        while True:
            try:
                choice = int(input())
                if choice < 1 or choice > r:
                    raise  exception
                break
            except:
                print('Enter a valid choice')

        if choice == 1:
            d = []
            while True:
                try:
                    num = int(input('\nEnter the number of values you will enter: '))
                    break
                except:
                    print('Enter a valid choice')
            if val == 3:
                print('\nEnter ' + str(num) + ' space separated date values (YYYY-MM-DD)')
            elif val == 4:
                print('\nEnter ' + str(num) + ' space separated time values (HH:MMAM or HH:MMPM) (should not have leading zeroes)') 
            else:
                print('\nEnter ' + str(num) + ' space separated values ')
            a = [i for i in input().split()]                
            if val == 4:
                for j in range(len(a)):
                    a[j] = a[j][:-2] + " " + a[j][-2:]

            for j in range(len(a)):
                l.append(f"""{column_list[i-1]} = '{a[j]}'""")
            l = '(' + ' OR '.join(l) + ')'

        
        if choice == 2:
            if val == 1:
                print('\nEnter range ( in the format:l r)')
            elif val == 3:
                print('\nEnter range ( in the format:l r  where l and r are date values YYYY-MM-DD')

            while True:
                try:
                    x, y = input().split()
                    break
                except:
                    print('Enter a valid choice')
            
            l = f"""({column_list[i-1]} BETWEEN '{x}' AND '{y}' )"""
            
        p.append(l)

    p = ' AND '.join(p)

    query += p

    try:
        cursor.execute(query);
    except:
        print("INVALID QUERY")
        return

    result = cursor.fetchall()

    header_list = []
    for u in b:
        header_list.append(column_list[u-1])

    print("\n\nRESULT:\n")
    print(tabulate(result, headers = header_list))
    

f = open('password.txt', 'rb')
str1 = pickle.load(f)
f.close()

def thirdpass(cursor):
    sq_q ="";
    while sq_q != 'exit':
        print("\nEnter your query (enter exit to break)")
        sq_q = input();
        if sq_q!= "exit":    
            print("\n")
            print("RESULT:\n")
            try:
                cursor.execute(sq_q);
                result = cursor.fetchall()
                columns = cursor.description
                column_list = []
                for c in columns:
                    column_list.append(c[0])

                print(tabulate(result, headers = column_list))

            except:
                print("\nCould not execute query")

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='digifam2',
                                         user='root',
                                         password= str1)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        cursor = connection.cursor(buffered = True)
        cursor.execute("select database();")

        print("Choose Mode\n")
        print("1.Basic (for a guest or user to show details)")
        print("2.Intermediate (for clerks, comapanies to give access to basic relational queries which they can create using options")
        print("3.Advanced (for administators to run custom queries)\n")

        while True:
            try:
                ch = int(input())
                if ch == 1:
                    onepass(cursor)
                elif ch == 2:
                    second_type_query(cursor)
                elif ch == 3:    
                    thirdpass(cursor)    
                if ch < 1 or ch > 3:
                    raise exception
                break
            except:
                print('Enter a valid choice')
        


except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")

