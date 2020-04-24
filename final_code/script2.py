import mysql.connector
from mysql.connector import Error
import pickle
import copy


def second_type_query(cursor):

    query = """drop table test;"""
    cursor.execute(query);

    # query = """show tables"""
    # cursor.execute(query);
    # result = cursor.fetchall()
    
    # query = """select * from family_folder;"""
    # cursor.execute(query)
    # result1 = cursor.fetchall()

    # query = """drop table family_folder;"""
    # cursor.execute(query)

    # query = """create table family_folder (
    # event_id varchar(8),
    # event_folder_url varchar(1000),
    # people_shared_id varchar(50)
    # );"""

    # cursor.execute(query);

    # # f = open('save.pkl', 'wb')
    # # pickle.dump(result1, f)
    # # f.close()

    # for row in result1:
    #     print(query)
    #     row = list(row)
    #     b = row[-1]
    #     b = b.split(',')
    #     for c in b:
    #         row1 = copy.deepcopy(row)
    #         row1[-1] = str(c).replace(" ", "")
    #         # row1[-1] = tuple(row[-1]) 
    #         row1 = tuple(row1)
    #         query = f"""insert into digifam2.family_folder values {row1};"""
    #         print(query)
    #         cursor.execute(query)
    #     # print(f"""{row}""")


    # print('Tables:', end = '\n\n')
    # for i in range(len(result)):
    #     print(str(i+1) + '. ' + result[i][0])


f = open('password.txt', 'rb')
str1 = pickle.load(f)
f.close()

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='digifam2',
                                         user='root',
                                         password= str1)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        cursor = connection.cursor(buffered = True)
        cursor.execute("select database();")
        
        second_type_query(cursor)    
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")

