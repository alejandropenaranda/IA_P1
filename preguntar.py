import tkinter as tk
import sys

# Funcion que muestra la segunda ventana con las opciones de busqueda informada
def mostrar_opciones():
    ventana.destroy()

    # Obtener la respuesta del usuario sobre el tipo de búsqueda
    respuesta = var.get()

    # Si el usuario eligio busqueda no informada
    if respuesta == "no informada":

        # Crear una nueva ventana
        ventana2 = tk.Tk()
        ventana2.geometry("200x130")
        ventana2.resizable(False, False)
        ventana2.eval('tk::PlaceWindow . center')

        ventana2.title("Opciones de busqueda no informada")
        
        # Crear una etiqueta con el texto"
        etiqueta2 = tk.Label(ventana2, text="Seleccione una opcion:")
        etiqueta2.pack()

        # Crear una variable para almacenar la opción elegida por el usuario
        var2 = tk.StringVar()
        var2.set(0)

        # Crear tres botones de radio con las opciones de costo, profundidad y amplitud
        radio1 = tk.Radiobutton(ventana2, text="Costo", variable=var2, value="costo")
        radio2 = tk.Radiobutton(ventana2, text="Profundidad", variable=var2, value="profundidad")
        radio3 = tk.Radiobutton(ventana2, text="Amplitud", variable=var2, value="amplitud")
        radio1.pack()
        radio2.pack()
        radio3.pack()

        # Crear una funcion que asigne el valor de la opcion elegida a una variable
        def enviar():
            global algoritmo
            algoritmo = var2.get()
            if algoritmo != 'costo' and algoritmo != 'amplitud' and algoritmo != 'profundidad':
                sys.exit()
            ventana2.destroy()
              
        # Crear un boton que llame a la funcion enviar
        boton2 = tk.Button(ventana2, text="Enviar", command=enviar)
        boton2.pack()
        
    elif respuesta == "informada":

        # Crear una nueva ventana
        ventana2 = tk.Tk()
        ventana2.geometry("200x130")
        ventana2.resizable(False, False)
        ventana2.eval('tk::PlaceWindow . center')

        # Asignar un titulo a la ventana
        ventana2.title("Opciones de busqueda informada")

        # Crear una etiqueta"
        etiqueta2 = tk.Label(ventana2, text="Seleccione una opcion:")

        # Colocar la etiqueta en la ventana
        etiqueta2.pack()

        # Crear una variable para almacenar la opción elegida por el usuario
        var2 = tk.StringVar()
        var2.set(0)

        # Crear 2 botones de radio con las opciones de avara y a*
        radio1 = tk.Radiobutton(ventana2, text="Avara", variable=var2, value="avara")
        radio2 = tk.Radiobutton(ventana2, text="a*", variable=var2, value="a*")

        # Colocar los botones de radio en la ventana
        radio1.pack()
        radio2.pack()

        # Crear una funcion que asigne el valor de la opcion elegida a una variable
        def enviar():
            global algoritmo
            algoritmo = var2.get()
            if algoritmo != 'avara' and algoritmo != 'a*':
                sys.exit()
            ventana2.destroy()
              
        # Crear un boton que llame a la funcion enviar cuando se haga clic en el
        boton2 = tk.Button(ventana2, text="Enviar", command=enviar)
        boton2.pack()
    else:
        sys.exit()
# Crea la ventana principal
ventana = tk.Tk()
ventana.geometry("400x130")
ventana.resizable(False, False)
ventana.eval('tk::PlaceWindow . center')
ventana.title("Algoritmo de búsqueda")

# Crear una etiqueta con el texto"
etiqueta = tk.Label(ventana, text="¿Desea utilizar un algoritmo de búsqueda informada o no informada?")
etiqueta.pack()

# Crear una variable para almacenar la respuesta del usuario
var = tk.StringVar()
var.set(0)

# Crear dos botones de radio con las opciones de informada y no informada
radio4 = tk.Radiobutton(ventana, text="Informada", variable=var, value="informada")
radio5 = tk.Radiobutton(ventana, text="No informada", variable=var, value="no informada")
radio4.pack()
radio5.pack()

# Crear un boton que llame a la funcion mostrar_opciones
boton = tk.Button(ventana, text="Continuar", command=mostrar_opciones)
boton.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()