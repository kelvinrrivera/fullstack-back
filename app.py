from flask import Flask
from flask import request
from flask import Flask, request, redirect

from persistencia import guardar_pedido
from flask import request

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def pedido_pizza():
    nombre = request.form.get("ifname")
    apellidos = request.form.get("ilname")

    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    print(nombre,apellidos)
    guardar_pedido(nombre,apellidos)
    
    return redirect("http://localhost/solicita_pedido.html", code=302)


