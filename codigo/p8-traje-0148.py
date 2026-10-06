import cv2

# Cambia esto:
# imagen = cv2.imread("../imagenes/traje-img-og-0148.jpg")

# Por esto (ruta desde la raíz del proyecto):
imagen = cv2.imread("imagenes/traje-img-og-0148.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original-Traje formal-0148", imagen)
cv2.imshow("Imagen suavizada-Traje formal-0148-Filtro Gaussiano", imagen_suavizada)

# Cambia esto:
# cv2.imwrite("../resultados/paisaje_gaussiano.jpg", imagen_suavizada)

# Por esto:
cv2.imwrite("resultados/paisaje_gaussiano.jpg", imagen_suavizada)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/paisaje_gaussiano.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Arath Valenzuela")
print("NC:0148")