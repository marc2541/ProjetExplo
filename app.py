from flask import Flask, render_template, request, url_for, redirect, jsonify
import psycopg2

app = Flask(__name__)


#
#   DATABASE SECTION
#

# Retourne une connection vers la BD
def get_db_connection():
    conn = psycopg2.connect(database="postgres", user="postgres", password="projet2SQL", host="mydbproj2.cemr0e3omd3i.us-east-2.rds.amazonaws.com", port="5432")
    
    # on peut laisser cette ligne au cas où on voudrait se connecter à une bd locale
    #conn = psycopg2.connect(database="postgres", user="postgres", password="admin")
    # use sql shell (psql) pour l'hoster local

    return conn

#
#   CONTROLLER SECTION
#

# Route : root
@app.route("/")
def index():
    return render_template('index.html')


# Route : Voir les livres que la bibliothèque contient
@app.route("/bibliothèque")
def bibliotheque():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM books ORDER BY id;')
    books = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('bibliotheque.html', books=books)

# Route : ajouter un livre
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('bibliotheque'))

    return render_template('create.html')



#
#   AJAX FUNCTION SECTION
#

@app.route("/ajax_delete_book",methods=["POST","GET"])
def ajax_delete():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM books WHERE id = {0}'.format(getid))
        conn.commit()

        cur.close()
        conn.close()
        
        msg = 'Livre supprimé avec succès'
    
    return jsonify(msg) 

if __name__ == "__main__":
    app.run(debug=True)