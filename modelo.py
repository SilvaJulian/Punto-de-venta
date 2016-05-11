# -*- coding: utf-8 -*-
import MySQLdb

class Consultas:

    def lista(self,lista):
        self.lista=lista
        bd=MySQLdb.connect("localhost","#usuario","#contraseña","#tabla de base de datos")
        cursor=bd.cursor()
        sql="SELECT nombre FROM productos"
        try:
            cursor.execute(sql)
            for i in cursor:
                resultado=cursor.fetchone()
                for j in resultado:
                    self.lista.append(j)
        except:
            print("error")
        bd.close()
        return self.lista

    def buscar_datos(self,nombre):
        self.nombre=nombre
        self.id_prod=''
        self.precio=''
        bd=MySQLdb.connect("localhost","#usuario","#contraseña","#tabla de base de datos")
        cursor=bd.cursor()
        sql="SELECT id,precios FROM productos WHERE nombre='%s'"%(self.nombre)
        try:
            cursor.execute(sql)
            for i in cursor:
                resultado=cursor.fetchone()
                for j in resultado:
                    if self.id_prod=='':
                        self.id_prod=j
                    else:
                        self.precio=j
        except:
            print("error")
        bd.close()
        return self.id_prod,self.precio


    def buscar_id(self,id_producto):
        self.nombre=''
        self.id_prod=int(id_producto)
        bd=MySQLdb.connect("localhost","#usuario","#contraseña","#tabla de base de datos")
        cursor=bd.cursor()
        sql="SELECT nombre FROM productos WHERE id='%i'"%(self.id_prod)
        try:
            cursor.execute(sql)
            for i in cursor:
                resultado=cursor.fetchone()
                for j in resultado:
                    self.nombre=j
        except:
            print("error")
        bd.close()
        return self.nombre

    def agregar_datos(self):
        print("%s,%s,%s")%(self.nombre,self.categoria,self.precio)
        bd=MySQLdb.connect("localhost","#usuario","#contraseña","#tabla de base de datos")
        cursor=bd.cursor()
        sql="INSERT INTO productos(nombre,descripcion,precios) VALUES('%s','%s',%.2f)"%(self.nombre.upper(),self.categoria.upper(),self.precio)
        cursor.execute(sql)
        bd.commit()
        bd.close()
        cursor.close()
        return
