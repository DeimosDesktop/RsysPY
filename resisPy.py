'''VISITA MI PÁGINA WEB PARA MÁS INFORMACIÓN:
https://mirpas.com
VISITA LA TEORÍA DEL NUEVO CURSO DE PYTHON PARA ELECTRÓNICOS:
https://mirpas.com/Lenguajes/4/2.php
'''
import tkinter as tk
from tkinter import Label, Frame, ttk, messagebox,Text,Menu
root = tk.Tk()
colores=["Negro","Marron", "Rojo","Naranja","Amarillo","Verde","Azul","Violeta","gris","blanco"]
root.geometry("505x370")
root.resizable(False,False)
root.title("Bienvenido a resisPY. Versión estudiante")
icono=tk.PhotoImage(file="ResisPY.png")
root.iconphoto(True, icono)
radioValue = tk.IntVar() 
valorResistenciaPorcentajeTemp = 0
valorToleranciaPorcentajeTemp = 0

######Cambiar color de fondo boton#####
def seleccionColor2(event):
    seleccion2= segundaBanda.current()
    '''messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=seleccion2
    )'''
    if seleccion2==0:
        boton2.configure(bg='black')
        mostrador.insert(1, "0")
        terceraBanda.configure(state="readonly")
    elif seleccion2==1:
        boton2.configure(bg="brown")
        mostrador.insert(1, "1")
        terceraBanda.configure(state="readonly")
    elif seleccion2==2:
        boton2.configure(bg="red")
        mostrador.insert(1, "2")
        terceraBanda.configure(state="readonly")
    elif seleccion2==3:
        boton2.configure(bg="orange")
        mostrador.insert(1, "3")
        terceraBanda.configure(state="readonly")
    elif seleccion2==4:
        boton2.configure(bg="yellow")
        mostrador.insert(1, "4")
        terceraBanda.configure(state="readonly")
    elif seleccion2==5:
        boton2.configure(bg="green")
        mostrador.insert(1, "5")
        terceraBanda.configure(state="readonly")
    elif seleccion2==6:
        boton2.configure(bg="blue")
        mostrador.insert(1, "6")
        terceraBanda.configure(state="readonly")
    elif seleccion2==7:
        boton2.configure(bg="violet")
        mostrador.insert(1, "7")
        terceraBanda.configure(state="readonly")
    elif seleccion2==8:
        boton2.configure(bg="grey")
        mostrador.insert(1, "8")
        terceraBanda.configure(state="readonly")
    elif seleccion2==9:
        boton2.configure(bg="white")
        mostrador.insert(1, "9")
        terceraBanda.configure(state="readonly")
    segundaBanda.configure(state="disabled")
def seleccionColor3(event):
    seleccion3= terceraBanda.current()
    '''messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=seleccion
    )'''
    if seleccion3==0:
        boton3.configure(bg='black')
        mostrador.insert(2,"Ω")
        tolerancia.configure(state="readonly")
    elif seleccion3==1:
        boton3.configure(bg="brown")
        mostrador.insert(2,"0Ω")
        tolerancia.configure(state="readonly")
    elif seleccion3==2:
        boton3.configure(bg="red")
        mostrador.insert(2,"00Ω")
        tolerancia.configure(state="readonly")
    elif seleccion3==3:
        boton3.configure(bg="orange")
        mostrador.insert(2,"KΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==4:
        boton3.configure(bg="yellow")
        mostrador.insert(2,"0KΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==5:
        boton3.configure(bg="green")
        mostrador.insert(2,"00KΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==6:
        boton3.configure(bg="blue")
        mostrador.insert(2,"MΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==7:
        boton3.configure(bg="violet")
        mostrador.insert(2,"0MΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==8:
        boton3.configure(bg="grey")
        mostrador.insert(2,"00MΩ")
        tolerancia.configure(state="readonly")
    elif seleccion3==9:
        boton3.configure(bg="white")
        mostrador.insert(2,"GΩ")
        tolerancia.configure(state="readonly")
    terceraBanda.configure(state="disabled")


def seleccionColor(event):
    seleccion = primeraBanda.current()
    '''messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=seleccion
    )'''
    ##Estructura para seleccionar colores##
    if seleccion==0:
        boton1.configure(bg='black')
        mostrador.delete(0,22)
        mostrador.insert(0, "0")
        segundaBanda.configure(state="readonly")
    elif seleccion==1:
        boton1.configure(bg="brown")
        mostrador.delete(0,22)
        mostrador.insert(0, "1")
        segundaBanda.configure(state="readonly")
    elif seleccion==2:
        boton1.configure(bg="red")
        mostrador.delete(0,22)
        mostrador.insert(0, "2")
        segundaBanda.configure(state="readonly")
    elif seleccion==3:
        boton1.configure(bg="orange")
        mostrador.delete(0,22)
        mostrador.insert(0, "3")
        segundaBanda.configure(state="readonly")
    elif seleccion==4:
        boton1.configure(bg="yellow")
        mostrador.delete(0,22)
        mostrador.insert(0, "4")
        segundaBanda.configure(state="readonly")
    elif seleccion==5:
        boton1.configure(bg="green")
        mostrador.delete(0,22)
        mostrador.insert(0, "5")
        segundaBanda.configure(state="readonly")
    elif seleccion==6:
        boton1.configure(bg="blue")
        mostrador.delete(0,22)
        mostrador.insert(0, "6")
        segundaBanda.configure(state="readonly")
    elif seleccion==7:
        boton1.configure(bg="violet")
        mostrador.delete(0,22)
        mostrador.insert(0, "7")
        segundaBanda.configure(state="readonly")
    elif seleccion==8:
        boton1.configure(bg="grey")
        mostrador.delete(0,22)
        mostrador.insert(0, "8")
        segundaBanda.configure(state="readonly")
    elif seleccion==9:
        boton1.configure(bg="white")
        mostrador.delete(0,22)
        mostrador.insert(0, "9")
        segundaBanda.configure(state="readonly")
    primeraBanda.configure(state="disabled")
    
def seleccionTolerancia(event):
   porcentajes = tolerancia.current()
   seleccionMultiplicador =terceraBanda.current()
   if porcentajes == 0:
       if seleccionMultiplicador ==0:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,3)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /100
           mostrador.insert(2, "+-")
           mostrador.insert(4, porcentaje)
           global valorResistenciaPorcentajeTemp
           global valorToleranciaPorcentajeTemp
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 1:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(3,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /100
           mostrador.insert(3, "+-")
           mostrador.insert(5, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 2:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(4,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /100
           mostrador.insert(4, "+-")
           mostrador.insert(6, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 3:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.1
           mostrador.insert(5, "KΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 4:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(3,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.1
           mostrador.insert(6, "KΩ+-")
           mostrador.insert(8, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 5:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(4,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.1
           mostrador.insert(7, "KΩ+-")
           mostrador.insert(9, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 6:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.0001
           mostrador.insert(2, "MΩ+-")
           mostrador.insert(6, porcentaje) 
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 7:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.0001
           mostrador.insert(3, "MΩ+-")
           mostrador.insert(7, porcentaje) 
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 8:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.000001
           mostrador.insert(3, "00MΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*100000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 9:
           boton4.configure(bg="brown")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 1 /0.1
           mostrador.insert(3, "GΩ+-")
           mostrador.insert(7, porcentaje)
           mostrador.insert(12, "MΩ")
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje*10**6
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(valorToleranciaPorcentajeTemp))
   if porcentajes == 1:
       if seleccionMultiplicador ==0:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,3)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /100
           mostrador.insert(2, "+-")
           mostrador.insert(4, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 1:
           boton4.configure(bg="red")
           longitud = mostrador.delete(3,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /100
           mostrador.insert(3, "+-")
           mostrador.insert(5, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 2:
           boton4.configure(bg="red")
           longitud = mostrador.delete(4,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /100
           mostrador.insert(4, "+-")
           mostrador.insert(6, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 3:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.1
           mostrador.insert(5, "KΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 4:
           boton4.configure(bg="red")
           longitud = mostrador.delete(3,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.1
           mostrador.insert(6, "KΩ+-")
           mostrador.insert(8, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 5:
           boton4.configure(bg="red")
           longitud = mostrador.delete(4,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.1
           mostrador.insert(7, "KΩ+-")
           mostrador.insert(9, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 6:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.0001
           mostrador.insert(2, "MΩ+-")
           mostrador.insert(6, porcentaje)  
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 7:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.0001
           mostrador.insert(3, "MΩ+-")
           mostrador.insert(7, porcentaje) 
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 8:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.000001
           mostrador.insert(3, "00MΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 9:
           boton4.configure(bg="red")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 2 /0.1
           mostrador.insert(3, "GΩ+-")
           mostrador.insert(7, porcentaje)
           mostrador.insert(12, "MΩ")
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje *1000000
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(valorToleranciaPorcentajeTemp))
   if porcentajes==2:
       if seleccionMultiplicador ==0:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,3)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /100
           mostrador.insert(2, "+-")
           mostrador.insert(4, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 1:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(3,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /100
           mostrador.insert(3, "+-")
           mostrador.insert(5, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 2:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(4,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /100
           mostrador.insert(4, "+-")
           mostrador.insert(6, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 3:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.1
           mostrador.insert(5, "KΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 4:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(3,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.1
           mostrador.insert(6, "KΩ+-")
           mostrador.insert(8, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 5:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(4,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.1
           mostrador.insert(7, "KΩ+-")
           mostrador.insert(9, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 6:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.0001
           mostrador.insert(2, "MΩ+-")
           mostrador.insert(6, porcentaje)  
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 7:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.0001
           mostrador.insert(3, "MΩ+-")
           mostrador.insert(7, porcentaje) 
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 8:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.000001
           mostrador.insert(3, "00MΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 9:
           boton4.configure(bg="gold")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 5 /0.1
           mostrador.insert(3, "GΩ+-")
           mostrador.insert(7, porcentaje)
           mostrador.insert(12, "MΩ")
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
   if porcentajes == 3:
       if seleccionMultiplicador ==0:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,3)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /100
           mostrador.insert(2, "+-")
           mostrador.insert(4, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 1:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(3,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /100
           mostrador.insert(3, "+-")
           mostrador.insert(5, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 2:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(4,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /100
           mostrador.insert(4, "+-")
           mostrador.insert(6, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 3:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.1
           mostrador.insert(5, "KΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 4:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(3,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.1
           mostrador.insert(6, "KΩ+-")
           mostrador.insert(8, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 5:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(4,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.1
           mostrador.insert(7, "KΩ+-")
           mostrador.insert(9, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 6:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.0001
           mostrador.insert(2, "MΩ+-")
           mostrador.insert(6, porcentaje)  
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 7:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,5)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.0001
           mostrador.insert(3, "MΩ+-")
           mostrador.insert(7, porcentaje) 
           valorResistenciaPorcentajeTemp = int(longitud)*1000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 8:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,6)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.000001
           mostrador.insert(3, "00MΩ+-")
           mostrador.insert(7, porcentaje)
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(porcentaje))
       elif seleccionMultiplicador == 9:
           boton4.configure(bg="silver")
           longitud = mostrador.delete(2,4)
           longitud = mostrador.get()
           porcentaje = int(longitud) * 10 /0.1
           mostrador.insert(3, "GΩ+-")
           mostrador.insert(7, porcentaje)
           mostrador.insert(12, "MΩ")
           valorResistenciaPorcentajeTemp = int(longitud)*1000000000
           valorToleranciaPorcentajeTemp = porcentaje*1000000
           #TESTER
           print("Valor de resistencia = {}. Tipo: {}".format(valorResistenciaPorcentajeTemp,
                                                               type(valorResistenciaPorcentajeTemp)))
           print("Valor de la Tolerancia = {}".format(valorToleranciaPorcentajeTemp))
   tolerancia.configure(state="disabled")
   radUno.configure(state="normal")
   radOs.configure(state="normal")
   radTres.configure(state="normal") 
       
   
   '''print(type(longitud))
   
   messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=porcentaje)'''
    
###################
#####CONTROLES#####
###################

########FRAMES######
resistencia = ttk.Frame(root)
resistencia.pack(side="top", ipadx="100", pady="20")
sistemaRKM = ttk.Frame(root)
sistemaRKM.pack(side="right", padx="10",ipady="200")
tituloRKM = ttk.LabelFrame(sistemaRKM, text="Sistema RKB",width=150,height=200)
tituloRKM.pack()
normalizacion = ttk.Frame(root)
normalizacion.pack(side="bottom", padx="1",ipady="10")
tituloNorma = ttk.LabelFrame(normalizacion, text="Normalización",width=200,height=200)
tituloNorma.pack()
#ESTOS LABEL SE PONEN AQUI PARA QUE APAREZCAN SOBRE LOS RADIO
normalizacionTitle = ttk.Label(tituloNorma,text="Familias de resistencias", background="light blue")
normalizacionTitle.pack(side="top")
familiaRadio = ttk.Frame(tituloNorma)
familiaRadio.pack()
########BOTONES y LABEL####
linea = tk.Label(resistencia,text="____________",padx="1",pady="8")
linea.pack(side="left")
boton1 = tk.Button(resistencia,bg="#EDEAE9",padx=15, pady=10, state="disabled")
boton1.pack(side="left")
boton2 = tk.Button(resistencia,bg="#EDEAE9", padx=15,pady=10, state="disabled")
boton2.pack(side="left")
boton3 = tk.Button(resistencia,bg="#EDEAE9", padx=15, pady=10, state="disabled")
boton3.pack(side="left")
boton4 = tk.Button(resistencia,bg="#EDEAE9",padx=15,pady=10, state="disabled")
boton4.pack(side="left")
linea2 = tk.Label(resistencia,text="_____________",padx="1",pady="8")
linea2.pack(side="left")
mostrador = tk.Entry(justify="center",font="30px")
mostrador.insert(0,"Pantalla de resultados")
mostrador.pack(side="top",padx="1",pady="10")

def reinicio():
    primeraBanda.configure(state="active")
    boton1.configure(bg="#EDEAE9")
    segundaBanda.configure(state="active")
    boton2.configure(bg="#EDEAE9")
    terceraBanda.configure(state="active")
    boton3.configure(bg="#EDEAE9")
    tolerancia.configure(state="active")
    boton4.configure(bg="#EDEAE9")
    mostrador.delete(0, 100)
    areaTexto.delete(1.0, "end")
botonReiniciar = ttk.Button(sistemaRKM, text="Reiniciar", command=reinicio)
botonReiniciar.pack(side="bottom",pady =30)
########COMBOBOX#######
color1 = ttk.Label(tituloRKM, text="Primera Banda")
color1.pack(side="top", ipadx="30")
primeraBanda = ttk.Combobox(tituloRKM,state="readonly",values=colores)
primeraBanda.bind("<<ComboboxSelected>>", seleccionColor)
primeraBanda.pack()
color2 = ttk.Label(tituloRKM, text="Segunda Banda")
color2.pack(side="top", ipadx="30")
segundaBanda = ttk.Combobox(tituloRKM,state="disabled",values=colores)
segundaBanda.bind("<<ComboboxSelected>>", seleccionColor2)
segundaBanda.pack()
color3 = ttk.Label(tituloRKM, text="Tercera Banda")
color3.pack(side="top", ipadx="30")
terceraBanda = ttk.Combobox(tituloRKM,state="disabled",values=colores)
terceraBanda.bind("<<ComboboxSelected>>", seleccionColor3)
terceraBanda.pack()
color4 = ttk.Label(tituloRKM, text="Tolerancia")
color4.pack(side="top", ipadx="30")
tolerancia = ttk.Combobox(tituloRKM, state="disabled", values=['Marrón','Rojo', 'Oro', 'Plata'])
tolerancia.bind("<<ComboboxSelected>>", seleccionTolerancia)
tolerancia.pack()
########RADIOBUTTONS#########
def E6():
   for a in range(6):
      print(valorToleranciaPorcentajeTemp)
      valor = 10 ** ((a - 1) / 6)* (valorResistenciaPorcentajeTemp /10)
      result1 = str(valor)
      print(type(result1))
      areaTexto.insert("1.0", result1+" Ω\n")
   radOs.configure(state="disabled")
   radTres.configure(state="disabled") 
   '''messagebox.showinfo(
        title="Pinchado radoibuton!",
        message="Seleccionado E6")'''

def E12():
    for a in range(12):
      print(valorToleranciaPorcentajeTemp)
      valor = 10 ** ((a - 1) / 12)* (valorResistenciaPorcentajeTemp /10)
      result1 = str(valor)
      print(type(result1))
      areaTexto.insert("1.0", result1+" Ω\n")
    radUno.configure(state="disabled")
    radTres.configure(state="disabled") 
 
def E24():
    for a in range(24):
      print(valorToleranciaPorcentajeTemp)
      valor = 10 ** ((a - 1) / 24)* (valorResistenciaPorcentajeTemp /10)
      result1 = str(valor)
      print(type(result1))
      areaTexto.insert("1.0", result1+" Ω\n")
    radOs.configure(state="disabled")
    radUno.configure(state="disabled") 

radUno = tk.Radiobutton(familiaRadio, text='E6', variable=radioValue, value="E6", command=E6, state="disabled") 
radUno.pack(side="left")
radOs = tk.Radiobutton(familiaRadio, text='E12', variable=radioValue, value="E12",command=E12, state="disabled") 
radOs.pack(side="left")
radTres = tk.Radiobutton(familiaRadio, text='E24', variable=radioValue, value="E24", command=E24, state="disabled")
radTres.pack(side="left")
#########TEXT#############
areaTexto = Text(tituloNorma,height = 8, width = 52,padx=10, pady=10, bd=5)
#areaTexto.tag_configure(tituloNorma,background="yellow", foreground="blue")
areaTexto.pack(side="top")
#########MENUS############
def salir():
    root.destroy()
barraMenus = Menu()
root.config(menu=barraMenus)
menuArchivo = Menu(tearoff=0)
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Guardar")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=salir)
barraMenus.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.post(300,10)
root.mainloop()