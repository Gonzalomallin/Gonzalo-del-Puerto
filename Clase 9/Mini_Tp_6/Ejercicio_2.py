inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}

for producto, info in inventario.items():
    if info["stock"] < 5:
        print(f"{producto} con stock bajo: {info["stock"]} unidades. ")

valor_total = sum(info["precio"] * info["stock"] for info in inventario.values())
print(f"El total del inventario es de ${valor_total}")

reposicion_urg = {producto for producto, info in inventario.items() if info["stock"] <= 2}
print(f"Necesita reponer urgentemente {reposicion_urg}")


