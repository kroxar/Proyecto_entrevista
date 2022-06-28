from cProfile import label
from tkinter import  messagebox, ttk
from tkinter import *
import tkinter.font as tkfont
import sqlite3


class product:
    
    db_nombre='la_perla.db'
    
    def __init__(self,window):        

        self.wind=window
        self.wind.title('LA PERLA') 
        
        # Creando frame contenedor nuevo registro
        frame=LabelFrame(self.wind, text='Registrar nuevo producto')
        frame.grid(row=0,column=0,columnspan=1,pady=0,padx=10)
        frame.config(font=('Ubuntu',15,'bold'))
       
        # Creando frame contenedor Buscar articulo
        frameBusqueda=LabelFrame(self.wind, text='Buscar artículo')
        frameBusqueda.grid(row=0,column=1,columnspan=1,pady=25,padx=10)
        frameBusqueda.config(font=('Ubuntu',15,'bold'))      
       
        # Texto Suma inventario
        self.labelSumainventario=Label(self.wind,text='Suma total del inventario: ')
        self.labelSumainventario.grid(row=6,column=3,sticky=W+E)
        self.labelSumainventario.config(font=('Ubunto',13,'bold'))
        
        # Input Suma total del inventario Solo lectura
        self.introsuma=StringVar()
        self.Sumatotalinventario=Entry(self.wind,textvariable=self.introsuma)
        self.Sumatotalinventario.grid(row=6,column=4,sticky=W+E)
        self.Sumatotalinventario.config(font=('Ubunto',13,'bold'))
        
        # Input Busqueda Código artículo
        labelCodigo=Label(frameBusqueda, text='Código Articulo: ')
        labelCodigo.grid(row=1,column=0)
        labelCodigo.config(font=('Ubunto',13))
        self.buscarCodigoarticulo=Entry(frameBusqueda)
        self.buscarCodigoarticulo.grid(row=1,column=1)
        
        # Input Busqueda nombre
        labelNombre=Label(frameBusqueda, text='Nombre Articulo: ')
        labelNombre.grid(row=2,column=0)
        labelNombre.config(font=('Ubunto',13))
        self.buscarnombreArticulo=Entry(frameBusqueda)
        self.buscarnombreArticulo.grid(row=2,column=1)
        
        # Input Código artículo
        labelCodigo=Label(frame, text='Código Articulo: ')
        labelCodigo.grid(row=1,column=0)
        labelCodigo.config(font=('Ubunto',13))
        self.CodigoArticulo=Entry(frame)
        self.CodigoArticulo.focus()
        self.CodigoArticulo.grid(row=1,column=1)
        
        # Input nombre
        labelNombre=Label(frame, text='Nombre Articulo: ')
        labelNombre.grid(row=2,column=0)
        labelNombre.config(font=('Ubunto',13))
        self.nombreArticulo=Entry(frame)
        self.nombreArticulo.grid(row=2,column=1)
        
        # Input Cantidad
        labelCantidad=Label(frame, text='Cantidad: ')
        labelCantidad.grid(row=3,column=0)
        labelCantidad.config(font=('Ubunto',13))
        self.cantidadArticulo=Entry(frame)
        self.cantidadArticulo.grid(row=3,column=1)
        
        # Input Precio
        labelPrecio=Label(frame, text='Precio Articulo: ')
        labelPrecio.grid(row=4,column=0)
        labelPrecio.config(font=('Ubunto',13))
        self.precioArticulo=Entry(frame)
        self.precioArticulo.grid(row=4,column=1)
        
        # Estilo Boton
        self.fontBoton=tkfont.Font(family='Ubuntu',size=12,weight='bold')
        
        # Boton Adicionar Guardar producto
        buttoAdicionarProducto=Button(frame,text='Guardar Producto',command=self.agregarArticulos)
        buttoAdicionarProducto.grid(row=5,column=0,columnspan=1,sticky=W + E)
        buttoAdicionarProducto['font']=self.fontBoton
        
        # Boton buscar Código
        buttonBuscar=Button(frameBusqueda,text='Buscar Codigo',command=self.buscarCodigo)
        buttonBuscar.grid(row=1,column=3,columnspan=1,sticky=W + E)
        buttonBuscar['font']=self.fontBoton
        
        # Boton buscar nombre
        buttonBuscar=Button(frameBusqueda,text='Buscar Nombre',command=self.buscarNombre)
        buttonBuscar.grid(row=2,column=3,columnspan=1,sticky=W + E) 
        buttonBuscar['font']=self.fontBoton
        
        #boton Inventario
        buttonInventario=Button(frameBusqueda,text='INVENTARIO',command=self.inventario)
        buttonInventario.grid(row=4,column=0,columnspan=2,sticky=W + E) 
        buttonInventario['font']=self.fontBoton
        
        # Boton Borrar 
        ButtonBorrar=Button(text='BORRAR',command=self.borrarProducto)
        ButtonBorrar.grid(row=6,column=0,sticky=W+E)
        ButtonBorrar['font']=self.fontBoton
        
        # Boton Editar
        ButtonEditar=Button(text='EDITAR',command=self.editarArticulo)
        ButtonEditar.grid(row=6,column=1,sticky=W+E)
        ButtonEditar['font']=self.fontBoton
        
        # Mensaje de salida
        self.mensaje =Label(text='',fg='red')
        self.mensaje.grid(row=4,column=0,columnspan=2,sticky=W+E)
        self.mensaje.config(font=('Ubuntu',20))
        
        ###############
        
        # Estilo de la tabla 
        estilo=ttk.Style()
        # Escoger tema (Puede ser = defauld,clam,alt,vista)
        estilo.theme_use('clam')
        # "Configuracion de color Treeview "
        estilo.configure('Treeview',
            background='silver',
            foreground='black',
            rowheight=35,
            fieldbackground='silver',
            font=('Ubuntu',13,'bold'))        
        # Cambio color al seleccionar
        estilo.map('Treeview',
            background=[('selected','blue')])
        ###############
        
        
        # Tabla
        columnas=('#1','#2','#3','#4','#5','#6')
        self.tabla = ttk.Treeview(self.wind,height=10,columns=columnas,show='headings')
        self.tabla.grid(row=5, column=0,columnspan=6) 
               
        self.tabla.heading('#1',text='Código',anchor=CENTER)
        self.tabla.heading('#2',text='Nombre',anchor=CENTER)
        self.tabla.heading('#3',text='Cantidad',anchor=CENTER)
        self.tabla.heading('#4',text='Precios unitario sin IVA',anchor=CENTER)
        self.tabla.heading('#5',text='Precios unitario con IVA',anchor=CENTER)
        self.tabla.heading('#6',text='Precios total por cantidad sin IVA',anchor=CENTER)
        
        # Llenando las filas de la tabla
        self.obtenerProductos()
    
    
    # Ejecutar consulta
    def ejecutarConsulta(self,consulta,parametros=()):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            resultado=cursor.execute(consulta,parametros)
            conn.commit()            
            return resultado
        
    #  Mostrar productos
    def obtenerProductos(self):
        
        # Limpiar tabla
        record=self.tabla.get_children()
        for elementos in record:
            self.tabla.delete(elementos)             
            
        # consulta
        consulta='SELECT * FROM productos'
        dbColumnas=self.ejecutarConsulta(consulta)
        sumainventario=0        
        for fila in dbColumnas:
            self.tabla.insert('',0,text=fila[1],values=(fila[0],fila[1],fila[2],fila[3],fila[3]+round(fila[3]*.19),fila[3]*fila[2]))
            sumainventario+=fila[3]*fila[2]
        sumainventario=str(sumainventario)
        self.introsuma.set('{} {}'.format("$",sumainventario))
        
    # Validar informacion "Los entry no esten vacios"
    def validarInformacion(self):
        return len(self.nombreArticulo.get())!=0 and len(self.precioArticulo.get())!=0 and len(self.cantidadArticulo.get())!= 0 
    
    # Buscar por codigo
    def buscarCodigo(self):
        
        # Limpiar mensaje
        self.mensaje['text']=''
        
        # Limpiar tabla
        record=self.tabla.get_children()
        for elementos in record:
            self.tabla.delete(elementos)            
   
        if len(self.buscarCodigoarticulo.get())!=0 :            
            parametro=(self.buscarCodigoarticulo.get(),)
            consulta='SELECT * FROM productos WHERE 1=1 AND codigo = ?'        
            resultado=self.ejecutarConsulta(consulta,parametro)
            for fila in resultado:
                self.tabla.insert('',0,text=fila[1],values=(fila[0],fila[1],fila[2],fila[3],fila[3]+round(fila[3]*.19),fila[3]*fila[2]))  
               
        else:
            self.mensaje['text']='Se debe ingresar el "Código Artículo "'
            self.buscarCodigoarticulo.delete(0,END)
            self.buscarnombreArticulo.delete(0,END)
            self.obtenerProductos()
        
    def buscarNombre(self):
        # Limpiar mensaje
        self.mensaje['text']=''
                
        # Limpiar tabla
        record=self.tabla.get_children()
        for elementos in record:
            self.tabla.delete(elementos) 
            
        if len(self.buscarnombreArticulo.get())!=0 :
            parametro=(self.buscarnombreArticulo.get(),)
            consulta='SELECT * FROM productos WHERE articulo = ?'        
            resultado=self.ejecutarConsulta(consulta,parametro)
            for fila in resultado:
                self.tabla.insert('',0,text=fila[1],values=(fila[0],fila[1],fila[2],fila[3],fila[3]+round(fila[3]*.19),fila[3]*fila[2]))
            
        else:
            self.mensaje['text']='Se debe ingresar el "Nombre Artículo "'
            self.buscarCodigoarticulo.delete(0,END)
            self.buscarnombreArticulo.delete(0,END)
            self.obtenerProductos()
        
    def inventario(self):
        self.obtenerProductos()
        # Limpiar mensaje
        self.mensaje['text']=''
            
    # Agregar Articulo
    def agregarArticulos(self):
        
        # Limpiar mensaje
        self.mensaje['text']=''  
        
        if self.validarInformacion():
            consulta='INSERT INTO productos VALUES(?,?,?,?)'
            parametros=(self.CodigoArticulo.get(),self.nombreArticulo.get(),self.cantidadArticulo.get(),self.precioArticulo.get())
            self.ejecutarConsulta(consulta,parametros)
            print('Datos guardados')
            self.mensaje['text']='Articulo {} se adicionó satisfactoriamente'.format(self.nombreArticulo.get())
            self.CodigoArticulo.delete(0,END)
            self.nombreArticulo.delete(0,END)
            self.cantidadArticulo.delete(0,END)
            self.precioArticulo.delete(0,END)
        
            
        else:
            # messagebox.showwarning(message='Nombre, precio y cantidad son requeridos',title='Espacios vacios')
            self.obtenerProductos()
            self.mensaje['text']='Nombre y precio del artículo son requeridos'
        self.obtenerProductos()
    
    # Borrar registro seleccionado        
    def borrarProducto(self):
        
        # Limpiar mensaje
        self.mensaje['text']=''
        # print(self.tabla.item(self.tabla.selection()))
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text']='Por favor selecciona un artículo'
            return
        # Limpiar mensaje
        self.mensaje['text']=''
        
        nombre=self.tabla.item(self.tabla.selection())['text']
        consulta='DELETE FROM productos WHERE  articulo = ?'        
        self.ejecutarConsulta(consulta,(nombre,))
        self.mensaje['text']='El dato {} ha sido eliminado'.format(nombre)
        self.obtenerProductos()
        
    # Editar registo seleccionado
    def editarArticulo(self):
        
        # Limpiar mensaje
        self.mensaje['text']=''        
        
        # editar mientras se seleccione un artículo
        self.mensaje['text']=''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text']='Por favor selecciona un artículo'
            return
        
        # Limpiar mensaje
        self.mensaje['text']=''
        
        codigoAntiguo=self.tabla.item(self.tabla.selection())['values'][0]
        nombre=self.tabla.item(self.tabla.selection())['text']        
        
        cantidadAntigua=self.tabla.item(self.tabla.selection())['values'][2]
        precioAntiguo=self.tabla.item(self.tabla.selection())['values'][3]
        self.editarVentan=Toplevel()
        self.editarVentan.title='Editar artículo'
        
        
        # Codigo antiguo
        laveCodigoAntiguo=Label(self.editarVentan, text='Código antiguo: ')
        laveCodigoAntiguo.grid(row=0,column=1)
        laveCodigoAntiguo.configure(font=('Ubunto',13))
        antiguoCodigo=Entry(self.editarVentan, textvariable=StringVar(self.editarVentan,value=codigoAntiguo),state='readonly')
        antiguoCodigo.grid(row=0,column=2)
        antiguoCodigo.configure(font=('Ubunto',13,'bold'))
        
        # Codigo nuevo
        lavelCodigoNuevo=Label(self.editarVentan, text='Código nuevo: ')
        lavelCodigoNuevo.grid(row=1,column=1)
        lavelCodigoNuevo.configure(font=('Ubunto',13))
        codigoNuevo=Entry(self.editarVentan,font=('Ubunto',13,'bold'))
        codigoNuevo.focus()
        codigoNuevo.grid(row=1,column=2)
        
        # Nombre antiguo
        lavelNombreAntiguo=Label(self.editarVentan, text='Nombre antiguo: ')
        lavelNombreAntiguo.grid(row=2,column=1)
        lavelNombreAntiguo.configure(font=('Ubunto',13))
        antiguoNombre=Entry(self.editarVentan, textvariable=StringVar(self.editarVentan,value=nombre),state='readonly')
        antiguoNombre.grid(row=2,column=2)
        antiguoNombre.configure(font=('Ubunto',13,'bold'))
        
        # Nombre nuevo
        lavelNombreNuevo=Label(self.editarVentan, text='Nombre nuevo: ')
        lavelNombreNuevo.grid(row=3,column=1)
        lavelNombreNuevo.configure(font=('Ubunto',13))
        nuevoNombre=Entry(self.editarVentan,font=('Ubunto',13,'bold'))
        nuevoNombre.grid(row=3,column=2)
        
        # Cantidad antigua
        lavelCantidadAntigua=Label(self.editarVentan, text='Cantidad antigua: ')
        lavelCantidadAntigua.grid(row=4,column=1)
        lavelCantidadAntigua.configure(font=('Ubunto',13))
        antiguaCantidad=Entry(self.editarVentan, textvariable=StringVar(self.editarVentan,value=cantidadAntigua),state='readonly')
        antiguaCantidad.grid(row=4,column=2)
        antiguaCantidad.configure(font=('Ubunto',13,'bold'))
        
        # Cantidad Nueva
        lavelCantidadNueva=Label(self.editarVentan, text='Cantidad nueva: ')
        lavelCantidadNueva.grid(row=5,column=1)
        lavelCantidadNueva.configure(font=('Ubunto',13))        
        nuevaCantidad=Entry(self.editarVentan,font=('Ubunto',13,'bold'))
        nuevaCantidad.grid(row=5,column=2)
        
        # Precio Antiguo
        lavelPrecioAntiguo=Label(self.editarVentan, text='Precio antiguo: ')
        lavelPrecioAntiguo.grid(row=6,column=1)
        lavelPrecioAntiguo.configure(font=('Ubunto',13))    
        antiguoPrecio=Entry(self.editarVentan, textvariable=StringVar(self.editarVentan,value=precioAntiguo),state='readonly')
        antiguoPrecio.grid(row=6,column=2)
        antiguoPrecio.configure(font=('Ubunto',13,'bold'))
        
        # Precio Nuevo
        lavelPrecioNuevo=Label(self.editarVentan,text='Precio nuevo: ')
        lavelPrecioNuevo.grid(row=7,column=1)
        lavelPrecioNuevo.configure(font=('Ubunto',13)) 
        nuevoPrecio=Entry(self.editarVentan,font=('Ubunto',13,'bold'))
        nuevoPrecio.grid(row=7,column=2)
        
        
        # boton actualiza 
        buttonActualizar=Button(self.editarVentan,text='Actualizar',command=lambda:self.actualizarArticulo(codigoNuevo.get(),nuevoNombre.get(),nuevaCantidad.get(),nuevoPrecio.get(),antiguoCodigo.get(),antiguoNombre.get(),antiguaCantidad.get(),antiguoPrecio.get()))
        buttonActualizar.grid(row=8,column=2,columnspan=2,sticky=W+E)
        buttonActualizar['font']=self.fontBoton
    
    # Actualizar registro seleccionado
    def actualizarArticulo(self,nuevoCodigo,nuevoArticulo,nuevaCantidad,nuevoPrecio,antiguoCodigo,antiguoNombre,antiguaCantidad,antiguoPrecio):
        
        # Limpiar mensaje
        self.mensaje['text']=''
        
        if len(nuevoArticulo)!=0 and len(nuevaCantidad)!=0 and len(nuevoPrecio)!=0 and len(nuevoCodigo)!=0: 
            consulta='UPDATE productos SET codigo = ?, articulo = ?, cantidad = ?, precio = ? WHERE codigo = ? AND articulo = ? AND cantidad = ? AND precio = ?' 
            parametros=(nuevoCodigo,nuevoArticulo,nuevaCantidad,nuevoPrecio,antiguoCodigo,antiguoNombre,antiguaCantidad,antiguoPrecio)
            try:
                self.ejecutarConsulta(consulta,parametros)
                self.editarVentan.destroy()
                self.mensaje['text']='Se ha editado el artículo {} satisfactoriamente'.format(antiguoNombre)
                self.obtenerProductos()
            except:
                messagebox.showwarning(message='Código del artículo ya existe')
        else:
                messagebox.showwarning(message='Llenar todos los campos',title='Campos incompletos')
        self.obtenerProductos()


if __name__=='__main__':
    
     
    window = Tk()
    aplication = product(window)
      
    window.mainloop()
    

