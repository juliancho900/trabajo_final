import Pyro4
import random
import json
import time
import os
import MySQLdb
import datetime

@Pyro4.expose
class Funcion():
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASS = ''
    DB_NAME = 'cinema'

    def run_query(self,query=''):
        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]

        conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
        cursor = conn.cursor()  # Crear un cursor
        cursor.execute(query)  # Ejecutar una consulta

        if query.upper().startswith('SELECT'):
            data = cursor.fetchall()  # Traer los resultados de un select
        else:
            conn.commit()  # Hacer efectiva la escritura de datos
            data = None

        cursor.close()  # Cerrar el cursor
        conn.close()

        return data

    def creartxt(self):
        archivo = open('datos.txt', 'w')
        archivo.close()

    def validar_usuario(self, cadena):
        x = [[cadena]]
        query = "SELECT correo FROM usuario WHERE correo = '%s'" % cadena
        result = self.run_query(query)
        user = json.dumps(x)
        y = json.dumps(result)
        if (y == user):
            self.creartxt()
            archivo = open('datos.txt', 'a')
            fecha = time.strftime("%x")
            hora = time.strftime("%X")
            archivo.write("Usuario " + cadena + '\n')
            archivo.write("Fecha " + fecha + '\n')
            archivo.write("Hora " + hora + '\n')
            archivo.close()
            return True

        else:
            self.creartxt()
            archivo = open('datos.txt', 'a')
            fecha = time.strftime("%x")
            hora = time.strftime("%X")
            archivo.write("Usuario " + cadena + '\n')
            archivo.write("Fecha " + fecha + '\n')
            archivo.write("Hora " + hora + '\n')
            archivo.close()
            return False

    def validar_contrasena(self, cadena):
        x = [[cadena]]
        query = "SELECT contrasena FROM usuario WHERE  contrasena = '%s' " % (cadena)
        result = self.run_query(query)
        user = json.dumps(x)
        y = json.dumps(result)
        if (y == user):
            return True
        else:
            return False

    def validar_clase(self,cadena):
        lista = [['administrador']]
        query = "SELECT tipo_usuario FROM usuario WHERE  contrasena = '%s' " % (cadena)
        result = self.run_query(query)
        user = json.dumps(result)
        y = json.dumps(lista)
        if (y == user):
            return True
        else:
            return False


    def actualizar_pelicula(self,b2,b1):
        query = "UPDATE pelicula SET nom_pelicula='%s' WHERE nom_pelicula = '%s'" % (b2,b1)
        self.run_query(query)
        return True

    def agregar_pelicula(self,dato, dato2, dato3):
        query = "INSERT INTO pelicula (nom_pelicula,valor_taquilla,sillas_disponibles) VALUES ('%s','%s','%s')" % (
        dato, dato2, dato3)
        self.run_query(query)
        return True

    def crea_usuario(self,user, cedula, tipo, correo, contra):
        fecha = datetime.date.today()
        z = fecha.strftime("%d/%m/%y")
        query = "INSERT INTO usuario (id_cedula,nombre_usuario,tipo_usuario,correo,contrasena,fecha_registro) VALUES ('%s','%s','%s','%s','%s','%s')" % (
        cedula, user, tipo, correo, contra, z)
        self.run_query(query)

        return True

    def generar_factura(self,pelicula, silla, horario, pago):
        persona = "Julian"
        fecha = time.strftime("%x")
        hora = time.strftime("%X")

        sillas = int(silla)
        valor = 10000 * sillas

        query = "INSERT INTO facturacion(nombre_pelicula,nombre_cliente,cupos_pelicula,horario_venta,fecha_venta,valor_taquilla) VALUES ('%s','%s','%s','%s','%s','%s')" % (
        pelicula, persona, silla, hora, fecha, str(valor))
        self.run_query(query)

        puntos = valor / 100
        query = "INSERT INTO puntos(nombre_cliente,puntos_cliente) VALUES ('%s','%s')" % (persona, str(puntos))
        self.run_query(query)
        return True

    def cambiar_puntos(self,producto):
        comprador ="Julian"
        query = "SELECT puntos_cliente FROM puntos WHERE nombre_cliente = '%s'" % comprador
        result = self.run_query(query)
        cadena = json.dumps(result)

        query = "SELECT puntos_producto FROM productos WHERE nombre_producto = '%s'" % producto
        result = self.run_query(query)
        b = json.dumps(result)
        if cadena == b:
            return True
            lista = ["sus puntos fueron canjeados exitosamente y presione enter >>"]
        else:
            lista = ["no tiene suficientes puntos, siga comprando y presione enter >>"]
        n = json.dumps(lista)
        return n




def main():
    demonio = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = demonio.register(Funcion)
    ns.register("julian.com", uri)
    demonio.requestLoop()

if __name__ == '__main__':
    main()


