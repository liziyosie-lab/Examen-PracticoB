from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# PUNTO 3: Creación de la base de datos y la tabla
def init_db():
    conn = sqlite3.connect('citas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            edad INTEGER,
            dueno TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# PUNTO 4: Rutas para mostrar y registrar pacientes
@app.route('/')
def index():
    conn = sqlite3.connect('citas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    lista_pacientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', pacientes=lista_pacientes)

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    especie = request.form['especie']
    edad = request.form['edad']
    dueno = request.form['dueno']
    
    conn = sqlite3.connect('citas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pacientes (nombre, especie, edad, dueno) VALUES (?, ?, ?, ?)',
                   (nombre, especie, edad, dueno))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)