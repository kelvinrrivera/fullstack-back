""" App.py """

from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def pedido_pizza():
    """
    Registra pedido
    """
    nombre = request.form.get("ifname")
    apellidos = request.form.get("ilname")

    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    print(nombre,apellidos)
    guardar_pedido(nombre,apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad.
    """
    size = request.form.get("tamano")
    if size=="S":
        mensaje = "No Disponible"
    else:
        mensaje = "Disponible"

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
