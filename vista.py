#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import gettext
import wx.grid
from modelo import Consultas
from controlador import Controlador

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.MINIMIZE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.panel=wx.Panel(self)
        self.Titulo = wx.StaticText(self, wx.ID_ANY, _("Bienvenido"), style=wx.ALIGN_CENTRE)
        self.button_ventas = wx.Button(self, wx.ID_ANY, _("Ventas Productos"))
        self.Bind(wx.EVT_BUTTON, self.boton_ventas,self.button_ventas)
        self.button_agregar = wx.Button(self, wx.ID_ANY, _("Agregar Productos"))
        self.Bind(wx.EVT_BUTTON, self.boton_agregar,self.button_agregar)
        self.button_salir = wx.Button(self, wx.ID_ANY, _("Salir"))
        self.Bind(wx.EVT_BUTTON, self.boton_salir,self.button_salir)

        self.button_ventas.SetFocus()
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle(_("Software Ventas Pymes - juliansilva.9@gmail.com"))
        self.SetSize((800,600))
        self.Titulo.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        self.button_ventas.SetMinSize((140, 100))
        self.button_agregar.SetMinSize((140, 100))
        self.button_salir.SetMinSize((140, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.Titulo, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_3.Add(self.button_ventas, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_3.Add(self.button_agregar, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_3.Add(self.button_salir, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL, 50)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade


    def boton_ventas(self,event):
        ventas_frame=Ventas_frame(parent=self)
        ventas_frame.Centre()
        ventas_frame.Show()
        self.panel.Hide()

    def boton_agregar(self,event):
        agregar_frame=Agregar_frame(parent=self)
        agregar_frame.Centre()
        agregar_frame.Show()
        self.panel.Hide()

    def boton_salir(self,event):
        ret  = wx.MessageBox('Quieres salir del programa?', 'Question',
        wx.YES_NO | wx.NO_DEFAULT, self)

        if ret == wx.YES:
            self.Close(True)

class Ventas_frame(wx.Panel):

    def __init__(self,parent, **kwds):
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, parent, size=(800,600), **kwds)
        self.parent=parent
        lista=[]
        self.consulta=Consultas()
        self.controlador=Controlador()
        lista=self.consulta.lista(lista)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("ID"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "",style=wx.TE_PROCESS_ENTER)
        self.text_ctrl_1.SetMaxLength(2)
        self.text_ctrl_1.Bind(wx.EVT_TEXT_ENTER,self.control_id)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("NOMBRE"))
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=lista, style=wx.CB_SIMPLE)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("CANTIDAD: "))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "",style=wx.TE_PROCESS_ENTER)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("INGRESAR"))
        self.Bind(wx.EVT_BUTTON,self.boton_ingresar,self.button_1)
        self.button_2 = wx.Button(self, wx.ID_ANY, _("FACTURAR"))
        self.Bind(wx.EVT_BUTTON,self.boton_facturar,self.button_2)
        self.grid_1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("TOTAL : "))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("PAGA CON : "))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "",style=wx.TE_PROCESS_ENTER)
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("VUELTO : "))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "",style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER,self.limpiar_todo,self.text_ctrl_5)
        self.button_3 = wx.Button(self, wx.ID_ANY, _(u"ATR\xc1S"))
        self.Bind(wx.EVT_BUTTON, self.boton_atras,self.button_3)
        self.button_4 = wx.Button(self, wx.ID_ANY, _("SALIR"))
        self.Bind(wx.EVT_BUTTON, self.boton_salir,self.button_4)

        self.__set_properties()
        self.__do_layout()
        self.text_ctrl_1.SetFocus()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyPanel.__set_properties
        self.grid_1.CreateGrid(0, 5)
        self.grid_1.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
        self.grid_1.SetColLabelValue(0, _("ID"))
        self.grid_1.SetColSize(0, -1)
        self.grid_1.SetColLabelValue(1, _("NOMBRE"))
        self.grid_1.SetColSize(1, 160)
        self.grid_1.SetColLabelValue(2, _("CANTIDAD"))
        self.grid_1.SetColSize(2,-1)
        self.grid_1.SetColLabelValue(3, _("PRECIO UNITARIO"))
        self.grid_1.SetColSize(3,-1)
        self.grid_1.SetColLabelValue(4, _("PRECIO "))
        self.grid_1.SetColSize(4,-1)
        self.grid_1.SetMinSize((600, 220))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.label_1, 0, 0, 0)
        sizer_4.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_4.Add(self.label_2, 0, 0, 0)
        sizer_4.Add(self.combo_box_1, 0, 0, 0)
        sizer_4.Add(self.label_3, 0, 0, 0)
        sizer_4.Add(self.text_ctrl_2, 0, 0, 0)
        sizer_4.Add(self.button_1, 0, 0, 0)
        sizer_4.Add(self.button_2, 0, 0, 0)
        sizer_3.Add(sizer_4, 2, wx.TOP | wx.BOTTOM, 15)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(self.grid_1, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 15)
        sizer_5.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL, 30)
        sizer_5.Add(self.text_ctrl_3, 0, 0, 0)
        sizer_5.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL, 30)
        sizer_5.Add(self.text_ctrl_4, 0, 0, 0)
        sizer_5.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL, 30)
        sizer_5.Add(self.text_ctrl_5, 0, 0, 0)
        sizer_2.Add(sizer_5, 1, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_6.Add(self.button_3, 0, wx.RIGHT, 10)
        sizer_6.Add(self.button_4, 0, wx.LEFT, 10)
        sizer_2.Add(sizer_6, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_2, 1, wx.TOP, 15)
        self.SetSizer(sizer_1)
        # end wxGlade

    def boton_salir(self,event):
        ret  = wx.MessageBox('Quieres salir del programa?', 'Question',
        wx.YES_NO | wx.NO_DEFAULT, self)

        if ret == wx.YES:
            self.Close(True)
            self.parent.Close(True)

    def boton_atras(self,event):
        self.parent.panel.Show()
        self.Destroy()

    def control_id(self,event):
        self.id_producto=self.text_ctrl_1.GetValue()
        self.nombre=self.consulta.buscar_id(self.id_producto)
        self.combo_box_1.SetValue('%s'%(self.nombre))
        self.text_ctrl_2.SetFocus()


    def boton_facturar(self,event):
        self.text_ctrl_4.SetFocus()
        self.Bind(wx.EVT_TEXT_ENTER,self.facturar,self.text_ctrl_4)

    def facturar(self,event):
        if self.text_ctrl_4.GetValue()=='':
            self.text_ctrl_5.SetFocus()
        else:
            self.paga_con=self.text_ctrl_4.GetValue()
            self.vuelto=self.controlador.vuelto(self.paga_con,self.total)
            self.text_ctrl_5.AppendText('%s'%(self.vuelto))
            self.text_ctrl_5.SetFocus()


    def boton_ingresar(self,event):
        self.grid_1.AppendRows(1)
        aux=self.grid_1.GetNumberRows()
        self.nombre=self.combo_box_1.GetValue()
        self.cantidad=self.text_ctrl_2.GetValue()
        (id_producto,precio_unidad)=self.consulta.buscar_datos(self.nombre)
        self.precio=self.controlador.precio_cantidad(self.cantidad,precio_unidad)
        self.grid_1.SetCellValue(aux-1,0,str(id_producto))
        self.grid_1.SetCellValue(aux-1,1,self.nombre)
        self.grid_1.SetCellValue(aux-1,2,self.cantidad)
        self.grid_1.SetCellValue(aux-1,3,str(precio_unidad))
        self.grid_1.SetCellValue(aux-1,4,str(self.precio))

        total=self.text_ctrl_3.GetValue()
        self.total=self.controlador.precios_total(self.precio,total)
        self.text_ctrl_3.Clear()
        self.text_ctrl_3.AppendText('%s'%(self.total))
        self.limpiar_campos()
        self.text_ctrl_1.SetFocus()

    def limpiar_campos(self):
        self.text_ctrl_1.Clear()
        self.combo_box_1.SetValue("")
        self.text_ctrl_2.Clear()

    def limpiar_todo(self,event):
        aux=self.grid_1.GetNumberRows()
        self.grid_1.ClearGrid()
        aux=self.grid_1.GetNumberRows()
        for i in range(aux):
            self.grid_1.DeleteRows(i,0-1)
        self.text_ctrl_3.Clear()
        self.text_ctrl_5.Clear()
        self.text_ctrl_4.Clear()
        self.text_ctrl_1.SetFocus()




class Agregar_frame(wx.Panel):

    def __init__(self,parent, **kwds):
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, parent, size=(800,600), **kwds)
        self.parent=parent
        self.consulta=Consultas()
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("INGRESE NOMBRE: "))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("INGRESE CATEGORIA: "))
        categoria=['almacen','gaseosas','limpieza','lacteos']
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=categoria, style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("INGRESE PRECIO: "))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, _("AGREGAR"))
        self.Bind(wx.EVT_BUTTON, self.boton_agregar,self.button_1)
        self.button_2 = wx.Button(self, wx.ID_ANY, _("FINALIZAR"))
        self.Bind(wx.EVT_BUTTON,self.boton_finalizar,self.button_2)
        self.grid_1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.button_3 = wx.Button(self, wx.ID_ANY, _(u"ATR\xc1S"))
        self.Bind(wx.EVT_BUTTON, self.boton_atras,self.button_3)
        self.button_4 = wx.Button(self, wx.ID_ANY, _("SALIR"))
        self.Bind(wx.EVT_BUTTON, self.boton_salir,self.button_4)

        self.__set_properties()
        self.__do_layout()
        self.text_ctrl_1.SetFocus()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyPanel.__set_properties
        self.grid_1.AutoSizeColumns(setAsMin=True)
        self.grid_1.CreateGrid(0, 3)
        self.grid_1.EnableDragColSize(2)
        self.grid_1.EnableDragRowSize(0)
        self.grid_1.EnableDragGridSize(0)
        self.grid_1.SetGridLineColour(wx.Colour(192, 192, 192))
        self.grid_1.SetColLabelValue(0, _("NOMBRE"))
        self.grid_1.SetColSize(0,-1)
        self.grid_1.SetColLabelValue(1, _("CATEGORIA"))
        self.grid_1.SetColSize(1,-1)
        self.grid_1.SetColLabelValue(2, _("PRECIO"))
        self.grid_1.SetColSize(2,-1)
        self.grid_1.SetMinSize((340,100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 0, wx.LEFT, 10)
        sizer_3.Add(self.text_ctrl_1, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_3.Add(self.label_2, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_3.Add(self.combo_box_1, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_3.Add(self.label_3, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_3.Add(self.text_ctrl_2, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_2.Add(sizer_3, 0, wx.EXPAND , 0)
        sizer_4.Add(self.button_1, 0, wx.LEFT | wx.RIGHT, 1)
        sizer_4.Add(self.button_2, 0, wx.LEFT, 1)
        sizer_2.Add(sizer_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(self.grid_1, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_5.Add(self.button_3, 0, wx.RIGHT, 1)
        sizer_5.Add(self.button_4, 0, wx.LEFT, 1)
        sizer_2.Add(sizer_5, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_2, 1, wx.TOP | wx.EXPAND, 24)
        self.SetSizer(sizer_1)
        # end wxGlade

    def boton_salir(self,event):
        ret  = wx.MessageBox('Quieres salir del programa?', 'Question',
        wx.YES_NO | wx.NO_DEFAULT, self)

        if ret == wx.YES:
            self.Close(True)
            self.parent.Close(True)

    def boton_atras(self,event):
        self.parent.panel.Show()
        self.Destroy()

    def boton_agregar(self,event):
        self.grid_1.AppendRows(1)
        aux=self.grid_1.GetNumberRows()
        self.nombre=self.text_ctrl_1.GetValue()
        self.categoria=self.combo_box_1.GetValue()
        self.precio=self.text_ctrl_2.GetValue()
        self.grid_1.SetCellValue(aux-1,0,self.nombre)
        self.grid_1.SetCellValue(aux-1,1,self.categoria)
        self.grid_1.SetCellValue(aux-1,2,self.precio)
        self.limpiar()
        self.text_ctrl_1.SetFocus()

    def limpiar(self):
        self.text_ctrl_1.Clear()
        self.combo_box_1.SetValue("")
        self.text_ctrl_2.Clear()


    def boton_finalizar(self,event):
        aux=self.grid_1.GetNumberRows()
        aux=int(aux)
        for i in range(aux):
            self.consulta.nombre=self.grid_1.GetCellValue(i,0)
            self.consulta.categoria=self.grid_1.GetCellValue(i,1)
            self.consulta.precio=float(self.grid_1.GetCellValue(i,2))
            self.consulta.agregar_datos()

        self.limpiar()
        self.limpiar_campos()
        self.text_ctrl_1.SetFocus()



    def limpiar_campos(self):
        self.text_ctrl_1.Clear()
        self.combo_box_1.SetValue("")
        self.text_ctrl_2.Clear()

if __name__ == "__main__":
    gettext.install("app")

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = MainFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    frame_2.Center()
    app.MainLoop()