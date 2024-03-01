import psycopg2

database_name = 'postgres'
database_user = 'postgres'
password = 'mailiondev'
host = 'localhost'
port_num = '5432'


def create_table():
    conn = psycopg2.connect(dbname=database_name,
                            user=database_user,
                            password=password,
                            host=host,
                            port=port_num)

    print("connection Success")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE student (id serial, name text, age text, address text);
    ''')
    print("Table created")
    conn.commit()
    conn.close()


def insert_data(name, age, address):
    conn = psycopg2.connect(dbname=database_name,
                            user=database_user,
                            password=password,
                            host=host,
                            port=port_num)

    print("connection Success")
    cur = conn.cursor()
    query = '''INSERT INTO student (name, age, address) VALUES (%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    print("Data Inserted")
    conn.commit()
    conn.close()


def search_student_by_id(data_id):
    conn = psycopg2.connect(dbname=database_name,
                            user=database_user,
                            password=password,
                            host=host,
                            port=port_num)
    query = '''SELECT * from student where id = %s'''
    cur = conn.cursor()
    cur.execute(query, (data_id,))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    return row


def display_all():
    conn = psycopg2.connect(dbname=database_name,
                            user=database_user,
                            password=password,
                            host=host,
                            port=port_num)
    query = '''SELECT * from student;'''
    cur = conn.cursor()
    cur.execute(query)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data
