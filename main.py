from Transformaciones import Convertido2, Convertido1
from Proceso import Proceso

if __name__ == '__main__':

    # Leido de las imagenes
    imagen_1 = Convertido1.leido_de_iamgen("images/iron.jpg")
    imagen_2 = Convertido2.leido_de_iamgen("images/albert.jpg")

    # Conversion de las imagenes
    imagen_1_convertida = Convertido1.imagen_a_escala_de_grises(imagen_1)
    imagen_2_convertida = Convertido2.imagen_laplaciana(imagen_2)

    # Guardado de las imagenes
    Convertido1.guardar_imagen(imagen_1_convertida,"ironconvertida")
    Convertido2.guardar_imagen(imagen_2_convertida, "albertconvertido")

    # MENSAJES PARA PODER VER LAS VENTANAS
    print("EL PROYECTO CORRIO MUY BIEN CHAMO")
    print("Cierrra la ventana para ver la imagen procesada")
    print("el primero es a blanco y negro ")
    print("el segundo a laplaciano degradado")

    # Mostrar en ventana las imagenes
    Proceso.mostrar_imagen_en_ventana(nombre_de_la_ventana="original iron",imagen_a_mostrar=imagen_1)
    Convertido1.mostrar_imagen_en_ventana(nombre_de_la_ventana="blanco y negro", imagen_a_mostrar=imagen_1_convertida)
    Proceso.mostrar_imagen_en_ventana(nombre_de_la_ventana="original albert",imagen_a_mostrar=imagen_2)
    Convertido1.mostrar_imagen_en_ventana(nombre_de_la_ventana="laplaciano", imagen_a_mostrar=imagen_2_convertida)

