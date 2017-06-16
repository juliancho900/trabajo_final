#!/usr/bin/python
#-*- coding: utf-8 -*-

import Pyro4
from Tkinter import *
from functools import partial
import ttk
import tkFont
import getpass


class funcionamiento():
    def __init__(self):
        self.conexion="julian.com"
        self.raiz = Tk()
        self.raiz.geometry('500x200+500+50') #tamano pantalla
        self.raiz.resizable(0,0) #impide cambiar el tamano
        self.raiz.title("VALIDACION USUARIO")
        self.fuente = tkFont.Font(weight='bold')#fuente de letra
        self.etiq1 = ttk.Label(self.raiz,text="USER",
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="PASS",
                               font=self.fuente)
        self.mensa = StringVar()#valida usuario y contra y dependiendo del resultado asigna color
        self.etiq3 = ttk.Label(self.raiz, textvariable=self.mensa,
                               font=self.fuente,foreground='Red')
        self.usuario = StringVar()
        self.clave = StringVar()
        self.ctext1 = ttk.Entry(self.raiz,
                                textvariable=self.usuario, width=35)
        self.ctext2 = ttk.Entry(self.raiz,
                                textvariable=self.clave,
                                width=35,
                                show="x")

        self.separador = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.raiz, text="Enter",
                                 padding=(5, 5), command=self.entrar)

        self.boton2 = ttk.Button(self.raiz, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.raiz, text="Cancel",
                                 padding=(5, 5), command=quit)


        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=70)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=50)
        self.ctext2.place(x=150, y=80)

        self.separador.place(x=5, y=145, bordermode=OUTSIDE, height=20, width=420)
        self.boton1.place(x=50, y=160)
        self.boton2.place(x=170, y=160)
        self.boton3.place(x=290, y=160)
        self.ctext1.focus_set()#posicionamiento del cursor en las cajas

        self.raiz.mainloop()#muestra la ventana

    def entrar(self):

        final = Pyro4.Proxy("PYRONAME:"+self.conexion)
        usuario = final.validar_usuario(self.ctext1.get())
        if usuario == True:
            password = final.validar_contrasena(self.ctext2.get())
            if password == True:
                self.etiq3.configure(foreground='blue')
                self.mensa.set ("Acceso Correcto")
                clase = final.validar_clase(self.ctext2.get())
                if clase == True:
                    self.abrir()
                else:
                    self.cliente()
            else:
                self.etiq3.configure(foreground='red')
                self.mensa.set("Contrasena Incorrecta")

        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso Denegado")
    def borrar(self):
        pass
    def cancelar(self):
        pass


    def actualiza(self):

        final = Pyro4.Proxy("PYRONAME:"+self.conexion)
        x = self.ctext1.get()
        y = self.ctext2.get()
        usuario = final.actualizar_pelicula(x, y)
        print usuario
        if usuario == True:
            mensa = ttk.Label(self.menu, foreground='red', text="pelicula actualizada" + self.pelicula_ant.get(),font=self.fuente).place(x=200, y=120)
         #   print "Hola Mundo"
            #self.etiq3.configure(foreground='blue')
            #self.mensa.set ("Pelicula Actualizada")


        #else:
         #   pass
            #self.etiq3.configure(foreground='red')
            #self.mensa.set("Proceso Invalido")
    def borrar(self):
        pass
    def cancelar(self):
        pass


    def agrega(self):

        final = Pyro4.Proxy("PYRONAME:"+self.conexion)
        x = self.ctext1.get()
        y = self.ctext2.get()
        z = self.ctext3.get()


        usuario = final.agregar_pelicula(x,y,z)

        print usuario
        if usuario == True:
            mensa = ttk.Label(self.menu, foreground='red', text="pelicula agregada" + self.pelicula_agre.get(),font=self.fuente).place(x=200, y=160)
         #   print "Hola Mundo"
            #self.etiq3.configure(foreground='blue')
            #self.mensa.set ("Pelicula Actualizada")


        #else:
         #   pass
            #self.etiq3.configure(foreground='red')
            #self.mensa.set("Proceso Invalido")

    def borrar(self):
        pass
    def cancelar(self):
        pass

    def abrir(self):
        self.servidor = "julian.com"
        self.menu = Tk()
        self.menudesplegar = Menu(self.menu)
        self.menu_advertencia = Menu(self.menudesplegar, tearoff=0)
        self.menu_advertencia.add_command(label="Maximo Sillas alcanzadas", command=self.maximo)
        self.menu_advertencia.add_separator()
        self.menu_advertencia.add_command(label="Salir",command=self.raiz.quit)
        self.menudesplegar.add_cascade(label="Alertas", menu=self.menu_advertencia)
        self.menu_peliculas = Menu(self.menudesplegar,tearoff=0)
        self.menu_peliculas.add_command(label="Listado Peliculas", command=self.pelicula)
        self.menu_peliculas.add_separator()
        self.menu_peliculas.add_command(label="Agregar Pelicula", command=self.agregar_pelicula)
        self.menu_peliculas.add_separator()
        self.menu_peliculas.add_command(label="Actualizar Peliculas", command=self.actualizar_pelicula)
        self.menu_peliculas.add_separator()
        self.menu_peliculas.add_command(label="salir", command=self.pelicula)
        self.menu_peliculas.add_separator()
        self.menudesplegar.add_cascade(label="Peliculas", menu=self.menu_peliculas)

        self.menu_ventas = Menu(self.menudesplegar,tearoff=0)
        self.menu_ventas.add_command(label="Listado facturas", command= self)
        self.menu_ventas.add_separator()
        self.menu_ventas.add_command(label="Detalle Factura", command= self)
        self.menu_ventas.add_separator()
        self.menu_ventas.add_command(label="Ventas Totales Dia", command= self)
        self.menu_ventas.add_separator()
        self.menu_ventas.add_command(label="Salir", command= self)
        self.menu_ventas.add_separator()
        self.menudesplegar.add_cascade(label="Ventas", menu=self.menu_ventas)

        self.menu_usuario = Menu(self.menudesplegar, tearoff=0)
        self.menu_usuario.add_command(label="Listado Usuario", command= self)
        self.menu_usuario.add_separator()
        self.menu_usuario.add_command(label="Usuarios y Puntos", command= self)
        self.menu_usuario.add_separator()
        self.menu_usuario.add_command(label="Crear Usuario", command= self.crea_usuario)
        self.menu_usuario.add_separator()
        self.menu_usuario.add_command(label="Salir", command= self)
        self.menu_usuario.add_separator()
        self.menudesplegar.add_cascade(label="Usuario", menu=self.menu_usuario)

        self.menu_log_usuario = Menu(self.menudesplegar, tearoff=0)
        self.menu_log_usuario.add_command(label="Reportes", command= self)
        self.menu_log_usuario.add_separator()
        self.menu_log_usuario.add_command(label="Salir", command= self)
        self.menu_log_usuario.add_separator()
        self.menu_log_usuario.add_cascade(label="Log Usuario", menu=self.menu_log_usuario)


        self.menu.config(menu=self.menudesplegar)
        self.menu.geometry('460x500+500+50')
        self.menu.resizable(0,0)
        self.menu.title("Cinema Lola")

    def actualizar_pelicula(self):
        self.fuente = tkFont.Font(weight='bold')  # fuente de letra
        self.etiq1 = ttk.Label(self.menu, text="Peli a Cambiar",
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.menu, text="Pelicula Nueva",
                               font=self.fuente)
        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.menu, textvariable=self.mensa,
                               font=self.fuente, foreground='Red')
        self.pelicula_ant = StringVar()
        self.pelicula_new= StringVar()
        self.ctext1 = ttk.Entry(self.menu,
                                textvariable=self.pelicula_ant, width=35)
        self.ctext2 = ttk.Entry(self.menu,
                                textvariable=self.pelicula_new,
                                width=35)

        self.separador = ttk.Separator(self.menu, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.menu, text="Enter",
                                 padding=(5, 5), command=self.actualiza)

        self.boton2 = ttk.Button(self.menu, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.menu, text="Cancel",
                                 padding=(5, 5), command=self.cancelar)

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=70)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=50)
        self.ctext2.place(x=150, y=80)

        self.separador.place(x=25, y=25, bordermode=OUTSIDE, height=20, width=420)
        self.boton1.place(x=50, y=400)
        self.boton2.place(x=170, y=400)
        self.boton3.place(x=290, y=400)
        self.ctext1.focus_set()  # posicionamiento del cursor en las cajas

        self.menu.mainloop()  # muestra la ventana



    def agregar_pelicula(self):
        self.fuente = tkFont.Font(weight='bold')  # fuente de letra
        self.etiq1 = ttk.Label(self.menu, text="Nombre Pelicula",
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.menu, text="Valor Taquilla",
                               font=self.fuente)
        self.etiq4 = ttk.Label(self.menu, text="Sillas Disp.",
                               font=self.fuente)

        self.etiq3 = ttk.Label(self.menu, textvariable=self.mensa,
                               font=self.fuente, foreground='Red')

        self.pelicula_agre = StringVar()
        self.taquilla_pel = StringVar()
        self.sillas_pel = StringVar()

        self.ctext1 = ttk.Entry(self.menu,
                                textvariable=self.pelicula_agre, width=35)
        self.ctext2 = ttk.Entry(self.menu,
                                textvariable=self.taquilla_pel, width=35)
        self.ctext3 = ttk.Entry(self.menu,
                                textvariable=self.sillas_pel, width=35)


        self.separador = ttk.Separator(self.menu, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.menu, text="Enter",
                                 padding=(5, 5), command=self.agrega)

        self.boton2 = ttk.Button(self.menu, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.menu, text="Cancel",
                                 padding=(5, 5), command=self.cancelar)

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq4.place(x=30, y=120)
        self.etiq3.place(x=30, y=160)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.ctext3.place(x=150, y=122)

        self.separador.place(x=5, y=200, bordermode=OUTSIDE, height=30, width=420)
        self.boton1.place(x=50, y=230)
        self.boton2.place(x=170, y=230)
        self.boton3.place(x=290, y=230)
        self.ctext1.focus_set()  # posicionamiento del cursor en las cajas

        self.menu.mainloop()  # muestra la ventana



    def crea_usuario(self):
        self.fuente = tkFont.Font(weight='bold')  # fuente de letra
        self.etiq1 = ttk.Label(self.menu, text="Identificacion",
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.menu, text="Nombre",
                               font=self.fuente)
        self.etiq4 = ttk.Label(self.menu, text="Tipo Usuario",
                               font=self.fuente)
        self.etiq5 = ttk.Label(self.menu, text="Correo",
                               font=self.fuente)
        self.etiq6 = ttk.Label(self.menu, text="Contraseña",
                               font=self.fuente)


        self.etiq3 = ttk.Label(self.menu, textvariable=self.mensa,
                               font=self.fuente, foreground='Red')

        self.id_user = StringVar()
        self.nom_user = StringVar()
        self.type_user = StringVar()
        self.mail_user = StringVar()
        self.pas_user = StringVar()


        self.ctext1 = ttk.Entry(self.menu,
                                textvariable=self.id_user, width=35)
        self.ctext2 = ttk.Entry(self.menu,
                                textvariable=self.nom_user, width=35)
        self.ctext3 = ttk.Entry(self.menu,
                                textvariable=self.type_user, width=35)
        self.ctext4 = ttk.Entry(self.menu,
                                textvariable=self.mail_user, width=35)
        self.ctext5 = ttk.Entry(self.menu,
                                textvariable=self.pas_user, width=35)



        self.separador = ttk.Separator(self.menu, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.menu, text="Enter",
                                 padding=(5, 5), command=self.creacion)

        self.boton2 = ttk.Button(self.menu, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.menu, text="Cancel",
                                 padding=(5, 5), command=self.cancelar)

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq4.place(x=30, y=120)
        self.etiq5.place(x=30, y=160)
        self.etiq6.place(x=30, y=200)

        self.etiq3.place(x=30, y=280)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.ctext3.place(x=150, y=122)
        self.ctext4.place(x=150, y=162)
        self.ctext5.place(x=150, y=202)


        self.separador.place(x=5, y=300, bordermode=OUTSIDE, height=30, width=420)
        self.boton1.place(x=50, y=330)
        self.boton2.place(x=170, y=330)
        self.boton3.place(x=290, y=330)
        self.ctext1.focus_set()  # posicionamiento del cursor en las cajas

        self.menu.mainloop()  # muestra la ventana


    def creacion(self):

        final = Pyro4.Proxy("PYRONAME:"+self.conexion)
        x = self.ctext1.get()
        y = self.ctext2.get()
        z = self.ctext3.get()
        w = self.ctext4.get()
        a = self.ctext5.get()

        usuario = final.crea_usuario(x,y,z,w,a)
        print usuario
        if usuario == True:
            mensa = ttk.Label(self.menu, foreground='red', text="Usuario Creado" + self.mail_user.get(),font=self.fuente).place(x=200, y=240)



    def cliente(self):
        self.servidor = "julian.com"
        self.menu_cliente = Tk()
        self.menudesplegar = Menu(self.menu_cliente)
        self.menu_peliculas = Menu(self.menudesplegar, tearoff=0)
        self.menu_peliculas.add_command(label="Ver lista peliculas", command=self.pelicula)
        self.menu_peliculas.add_separator()
        self.menu_peliculas.add_command(label="Generar Factura", command=self.generar_factura)
        self.menu_peliculas.add_separator()
        self.menu_peliculas.add_command(label="Salir", command=self.menu_peliculas)
        self.menu_peliculas.add_separator()
        self.menudesplegar.add_cascade(label="compra pase", menu=self.menu_peliculas)

        self.menu_ventas = Menu(self.menudesplegar, tearoff=0)
        self.menu_ventas.add_command(label="Ver Puntos", command=self)
        self.menu_ventas.add_separator()
        self.menu_ventas.add_command(label="Cambiar Puntos", command=self.puntos)
        self.menu_ventas.add_separator()
        self.menu_ventas.add_command(label="Salir", command=self)
        self.menu_ventas.add_separator()
        self.menudesplegar.add_cascade(label="Puntos", menu=self.menu_ventas)

        self.menu_usuario = Menu(self.menudesplegar, tearoff=0)
        self.menu_usuario.add_command(label="Ver facturas", command=self)
        self.menu_usuario.add_separator()
        self.menu_usuario.add_command(label="detalles facturas", command=self)
        self.menu_usuario.add_separator()
        self.menu_usuario.add_command(label="Salir", command=self)
        self.menu_usuario.add_separator()
        self.menudesplegar.add_cascade(label="Facturas", menu=self.menu_usuario)

        self.menu_cliente.config(menu=self.menudesplegar)
        self.menu_cliente.geometry('460x500+500+50')
        self.menu_cliente.resizable(0, 0)
        self.menu_cliente.title("Cinema Lola")

    def generar_factura(self):
        self.fuente = tkFont.Font(weight='bold')  # fuente de letra
        self.etiq1 = ttk.Label(self.menu_cliente, text="Pelicula",
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.menu_cliente, text="Horario",
                               font=self.fuente)
        self.etiq3 = ttk.Label(self.menu_cliente, text="# Silla",
                               font=self.fuente)
        self.etiq4 = ttk.Label(self.menu_cliente, text="Pago Cliente",
                               font=self.fuente)

        self.etiq5 = ttk.Label(self.menu_cliente, textvariable=self.mensa,
                               font=self.fuente, foreground='Red')

        self.pelicula = StringVar()
        self.horario = StringVar()
        self.silla = StringVar()
        self.taquilla = StringVar()
        self.pago = StringVar()

        self.ctext1 = ttk.Entry(self.menu_cliente,
                                textvariable=self.pelicula, width=35)
        self.ctext2 = ttk.Entry(self.menu_cliente,
                                textvariable=self.horario, width=35)
        self.ctext3 = ttk.Entry(self.menu_cliente,
                                textvariable=self.silla, width=35)
        self.ctext4 = ttk.Entry(self.menu_cliente,
                                textvariable=self.pago, width=35)

        self.separador = ttk.Separator(self.menu_cliente, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.menu_cliente, text="Enter",
                                 padding=(5, 5), command=self.factura)

        self.boton2 = ttk.Button(self.menu_cliente, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.menu_cliente, text="Cancel",
                                 padding=(5, 5), command=self.cancelar)

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=30, y=120)
        self.etiq4.place(x=30, y=160)
        self.etiq5.place(x=30, y=200)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.ctext3.place(x=150, y=122)
        self.ctext4.place(x=150, y=162)

        self.separador.place(x=5, y=300, bordermode=OUTSIDE, height=30, width=420)
        self.boton1.place(x=50, y=330)
        self.boton2.place(x=170, y=330)
        self.boton3.place(x=290, y=330)
        self.ctext1.focus_set()  # posicionamiento del cursor en las cajas

        self.menu_cliente.mainloop()  # muestra


    def factura(self):

        final = Pyro4.Proxy("PYRONAME:" + self.conexion)
        pelicula = self.ctext1.get()
        horario = self.ctext2.get()
        silla = self.ctext3.get()
        pago = self.ctext4.get()

        usuario = final.generar_factura(pelicula, silla, horario,pago)
        if usuario == True:
            mensa = ttk.Label(self.menu_cliente, foreground='red', text="Factura Generada" + self.pelicula.get(),
                              font=self.fuente).place(x=200, y=240)


    def puntos(self):
        self.fuente = tkFont.Font(weight='bold')  # fuente de letra
        self.etiq1 = ttk.Label(self.menu_cliente, text="PRODUCTO",
                               font=self.fuente)
        self.mensa = StringVar()  # valida usuario y contra y dependiendo del resultado asigna color
        self.etiq2 = ttk.Label(self.menu_cliente, textvariable=self.mensa,
                               font=self.fuente, foreground='Red')
        self.producto = StringVar()
        self.ctext1 = ttk.Entry(self.menu_cliente,
                                textvariable=self.producto, width=35)


        self.separador = ttk.Separator(self.menu_cliente, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.menu_cliente, text="Enter",
                                 padding=(5, 5), command=self.cambiar)

        self.boton2 = ttk.Button(self.menu_cliente, text="Clear", padding=(5, 5), command=self.borrar)
        self.boton3 = ttk.Button(self.menu_cliente, text="Cancel",
                                 padding=(5, 5), command=self.cancelar)

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=70)
        self.ctext1.place(x=150, y=50)

        self.separador.place(x=5, y=145, bordermode=OUTSIDE, height=20, width=420)
        self.boton1.place(x=50, y=160)
        self.boton2.place(x=170, y=160)
        self.boton3.place(x=290, y=160)
        self.ctext1.focus_set()  # posicionamiento del cursor en las cajas

        self.menu_cliente.mainloop()  # muestra la ventana

    def cambiar(self):
        final = Pyro4.Proxy("PYRONAME:" + self.conexion)
        producto = self.ctext1.get()


        usuario = final.cambiar_puntos(producto)
        if usuario == True:
            mensa = ttk.Label(self.menu_cliente, foreground='red', text="Puntos Canjeados" + self.producto.get(),
                              font=self.fuente).place(x=150, y=120)
        else:
            mensa = ttk.Label(self.menu_cliente, foreground='red', text="Puntos No Canjeados" + self.producto.get(),
                              font=self.fuente).place(x=150, y=120)




    def pelicula(self):
        print "hola"
    def maximo(self):
        print "hola"
    def borrar(self):
        self.usuario.set("")
        self.clave.set("")


def main():
    julian = funcionamiento()


def conectar():
    servidor = "julian.com"
    final = Pyro4.Proxy("PYRONAME:"+ servidor)


if __name__ == '__main__':
    main()