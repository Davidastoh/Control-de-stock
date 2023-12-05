from funciones import insertar_producto

# Función para agregar productos a la base de datos
def agregar_producto():
    nombre = nombre_entry.get()
    cantidad = cantidad_entry.get()
    insertar_producto(nombre, cantidad)
    # Actualizar la interfaz o mostrar un mensaje de éxito

root = Tk()
root.title("Control de Stock")

nombre_label = Label(root, text="Nombre del producto:")
nombre_label.pack()
nombre_entry = Entry(root)
nombre_entry.pack()

cantidad_label = Label(root, text="Cantidad:")
cantidad_label.pack()
cantidad_entry = Entry(root)
cantidad_entry.pack()

agregar_button = Button(root, text="Agregar producto", command=agregar_producto)
agregar_button.pack()

root.mainloop()