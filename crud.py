#creating connection with database
import mysql.connector
try:
    conn = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            database = 'indigo')
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connection error')

#mycursor.execute("create database indigo") this is to be run only once because the table is created in the dtabase
#conn.commit()

#create a table
# by the name of ariport -id ,code ,name

#mycursor.execute('''                           this is to be run only once
#CREATE TABLE airport(
                    #airport_id INTEGER PRIMARY KEY,
                    #Code VARCHAR(10) NOT NULL,
                    #CITY VARCHAR(50) NOT NULL,
                   # name VARCHAR(255) NOT NULL)''')
#conn.commit()
# insert data to the table
#mycursor.execute("""
        #INSERT INTO airport VALUES
        #(1,'DEL','new delhi','IGIA'),
        #(2,'CCU','kolkata','NSCA'),
        #(3,'BOM','mumbai','CSMA')
    #""")
#conn.commit()

# search/retrieve
mycursor.execute('SELECT * FROM airport WHERE airport_id > 1')
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])


# update
mycursor.execute("""
                UPDATE airport
                SET name = 'Bombay'
                WHERE airport_id = 3
""")
conn.commit()

mycursor.execute('SELECT * FROM airport')
data = mycursor.fetchall()
print(data)

#delete
mycursor.execute("DELETE from airport WHERE airport_id = 3")
conn.commit()

mycursor.execute('SELECT * FROM airport')
data = mycursor.fetchall()
print(data)













