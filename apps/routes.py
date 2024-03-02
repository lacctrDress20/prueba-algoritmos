from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

class Ferreteria:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar_usuario(self, nombre, email, contraseña):
        nuevo_usuario = Usuario(nombre, email, contraseña)
        self.usuarios_registrados.append(nuevo_usuario)
        print(f"Usuario {nombre} registrado con éxito.")

ferreteria = Ferreteria()

@app.route("/")
def index():
    return render_template("registro.html")

@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    contraseña = request.form.get("contraseña")
    ferreteria.registrar_usuario(nombre, email, contraseña)
    return jsonify({"mensaje": "Usuario registrado con éxito."})

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/cancel_order")
def cancel_order():
    return render_template("cancel_order.html")

if __name__ == "__main__":
    app.run(debug=True)
