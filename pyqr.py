import qrcode

# Crear el objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Tamaño del código QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja del código QR
    border=4,  # Tamaño del borde del código QR
)

# Añadir los datos que quieres codificar
data = "https://github.com/edwinesco"
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill="black", back_color="white")

# Guardar la imagen
img.save("github_edwinesco.png")