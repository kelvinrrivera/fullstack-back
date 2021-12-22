def guardar_pedido(ifname,ilname):


    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(ifname + " " + ilname + "\n")
        file.close()
