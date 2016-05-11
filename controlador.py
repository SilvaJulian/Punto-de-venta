class Controlador():

    def precio_cantidad(self,cantidad,precio):
        self.cant=int(cantidad)
        self.precio=float(precio)
        self.total=self.cant * self.precio
        return self.total

    def precios_total(self,precio,total):
        self.precio_total=float(total)
        self.precio_total+=float(precio)
        return self.precio_total

    def vuelto(self,paga_con,total):
        self.paga_con=float(paga_con)
        self.total=float(total)
        self.vuelto=self.paga_con-self.total
        return self.vuelto