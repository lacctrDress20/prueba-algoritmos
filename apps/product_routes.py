import sqlite3
from flask import Flask, request, jsonify

# Conectar a la base de datos (SQLite creará el archivo si no existe)
conn = sqlite3.connect('productos.db')

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Lista de productos para agregar
nuevos_productos = [
    ("Martillo", "Martillo de acero inoxidable", 15.99),
    ("Destornillador", "Destornillador Phillips magnético", 9.99),
    ("Sierra circular", "Sierra circular de alta potencia", 129.99)
    ("Llave inglesa", "Llave ajustable de acero al carbono", 12.99),
    ("Destornillador eléctrico", "Destornillador eléctrico recargable", 39.99),
    ("Sierra de mano", "Sierra de mano portátil para cortes precisos", 19.99)
]

# Insertar los nuevos productos en la tabla de productos
for producto in nuevos_productos:
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)", producto)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Nuevos productos agregados exitosamente.")


# Crear una instancia de Flask
app = Flask(__name__)

# Ruta para buscar todos los productos
@app.route("/products", methods=["GET"])
def get_products():
    # Conectar a la base de datos
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    
    # Obtener el término de búsqueda del parámetro de la URL
    query = request.args.get('query')

    # Consulta SQL para obtener productos que coincidan con el término de búsqueda
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + query + '%',))
    productos = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conn.close()

    # Convertir los resultados en un formato JSON y devolverlos como respuesta
    return jsonify(productos)

if __name__ == "__main__":
    app.run(debug=True)
