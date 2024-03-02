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

if __name__ == "__main__":
    app.run(debug=True)
