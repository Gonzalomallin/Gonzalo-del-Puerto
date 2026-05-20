registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]

ciudades = set(reg[1] for reg in registros)
print("Ciudades sin repetir:", ciudades)

fechas = set(reg[0] for reg in registros)
print("Fechas sin repetir", fechas)

temp_ciudad = {}
for fechas, ciudades, temp in registros:
    if ciudades not in temp_ciudad:
        temp_ciudad[ciudades].append(temp)

prom_ciudad = {}
for ciudad, temps in temp_ciudad.items():
    prom_ciudad[ciudad] = sum(temps) / len(temps)
print("El promedio  de temperatura por ciudad: ")
for ciudad, promedio in promedios_ciudad.items():
    print(f" - {ciudad}: {promedio:.2f}°C")
ciudad_max_promedio = max(promedios_ciudad, key=promedios_ciudad.get)
print(f"La ciudad con el mayor promedio es: {ciudad_max_promedio} ({promedios_ciudad[ciudad_max_promedio]:.2f}°C)")










