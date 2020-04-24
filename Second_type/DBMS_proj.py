import mysql.connector
from mysql.connector import Error
import pickle


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
    print('\nSelect a table')
    ch = int(input())
    while ch < 1 or ch > len(result):
        print('Invalid Choice')
        print('\nSelect a table')
        ch = int(input())

    table = result[ch-1][0]
    
    query = f"""select column_name from information_schema.columns where table_name = '{table}'"""
    # print(query)
    cursor.execute(query);
    result = cursor.fetchall()

    # for row in result:
    #     print(row)

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

    print(b)
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
        
        if val == 1:
            r += 1    
            print(str(r) + '. Enter a range\n')

        choice = int(input())
        if choice == 1:
            d = []
            print('Enter the number of values you will enter')
            num = int(input())
            print('Enter ' + str(num) + ' space separated numbers')
            a = [int(i) for i in input().split()]                
            print(a)
            for j in range(len(a)):
                l.append(f"""{column_list[i-1]} = '{a[j]}'""")
            l = '(' + ' OR '.join(l) + ')'
        
        if choice == 2:
            print('Enter range ( in the format:l r)')
            x, y = input().split()

            l = f"""({column_list[i-1]} BETWEEN {x} AND {y})"""

            
        p.append(l)

    p = ' AND '.join(p)

    query += p
    print(query)

    cursor.execute(query);
    result = cursor.fetchall()

    for row in result:
        print(row)




f = open('password.txt', 'rb')
str1 = pickle.load(f)
f.close()

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='digifam',
                                         user='root',
                                         password= str1)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        cursor = connection.cursor(buffered = True)
        cursor.execute("select database();")
        


        second_type_query(cursor)    

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")

