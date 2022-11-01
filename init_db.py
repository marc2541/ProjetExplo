import os
import psycopg2

#
#       SCRIPT pour créer la BD et insert des données
#

#conn = psycopg2.connect(database="postgres", user="postgres", password="admin")
conn = psycopg2.connect(database="postgres", user="postgres", password="projet2SQL", host="mydbproj2.cemr0e3omd3i.us-east-2.rds.amazonaws.com", port="5432")
# conn = psycopg2.connect(
#         host="localhost",
#         database="postgres",
#         user=os.environ['postgres'],
#         password=os.environ['admin'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Hello world',
             'projet2',
             150,
             'Un classique!')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('TempleOS',
             'Monster energy drinks',
             864,
             'Un autre véritable classique!')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Red had',
             'Linus Torpille',
             864,
             'Le meilleur os pas possible')
            )

conn.commit()

cur.close()
conn.close()
