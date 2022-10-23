import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')



    connection.autocommit = True

    cursor = connection.cursor()

    create_table_query = ''' CREATE TABLE Registration 
            (id             INTEGER PRIMARY KEY,
            student_id      CHAR(13) NOT NULL,
             subject_id     VARCHAR(15) NOT NULL,     
             year           CHAR(4) NOT NULL,
             semester       CHAR(1)  NOT NULL,  
             grade          CHAR(2) NOT NULL);'''


        #Creating a database 
    cursor.execute(create_table_query)
    connection.commit()
    print("Database created successfully in PostgreSQL")


except (Exception, psycopg2.DatabaseError) as error : 
    print('Error while connectiong to PostgreSQL',error)
    
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    