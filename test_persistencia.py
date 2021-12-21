from persistencia import guardar_pedido
from flask import request


with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

ifname = request.form['ifname']
ilname = request.form['ilname']


guardar_pedido(ifname, ilname)
