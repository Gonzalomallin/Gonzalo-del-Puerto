cuenta_usuario = {
    "usuario": "Gonzalo",
    "email": "gonzalo@google.com",
    "activo": True
}

print(cuenta_usuario["email"])
cuenta_usuario["activo"] = False
print(cuenta_usuario["activo"])
cuenta_usuario["ultimo_login"] = (6, 5, 2026)
print(cuenta_usuario)
