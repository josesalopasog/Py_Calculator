from tkinter import *

operador = ''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    while True:
        try: 
            global operador
            resultado = str(eval(operador))
            visor_calculadora.delete(0, END)
            visor_calculadora.insert(0, resultado)
            operador = ''
            break
        except ZeroDivisionError:
            visor_calculadora.delete(0, END)
            visor_calculadora.insert(0,'Error')
            operador = ''
            break
        except SyntaxError:
            break
        
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1
        
#Iniciar Tkinter
aplicacion = Tk()

#Tamapaño de la ventana
aplicacion.geometry('1200x630+0+0')

#Evitar maximizar
aplicacion.resizable(0,0)

#Titulo de la ventana
aplicacion.title("Mi restaurante - Sistema de Facturación")

#Color de la ventana
aplicacion.config(bg = 'azure')

#Panel Superior
panel_superior = Frame(aplicacion, 
                       bd=1, 
                       relief=FLAT)
panel_superior.pack(side=TOP)
#----Etiqueta Titulo-----
etiqueta_titulo = Label(panel_superior, 
                        text='Sistema de Facturación', 
                        fg='black', 
                        font=('Dosis',58), 
                        bg ='azure',
                        width=27)

etiqueta_titulo.grid(row=0,column=0)

#Panel Izquierdo 
panel_izquierdo = Frame(aplicacion, bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel Costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg='azure4',padx=60)
panel_costos.pack(side=BOTTOM)

#Panel Comidas 
panel_comidas = LabelFrame(panel_izquierdo, 
                           text='Comida', 
                           font=('Dosis',19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='black')
panel_comidas.pack(side=LEFT)

#Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, 
                           text='Bebidas', 
                           font=('Dosis',19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='black')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, 
                           text='Postres', 
                           font=('Dosis',19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='black')
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel Calculadora
panel_calculadura = Frame(panel_derecha,bd=1,relief=FLAT,bg='azure')
panel_calculadura.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg='azure')
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg='azure')
panel_botones.pack()

#Lista de prodcutos
lista_comidas = ['pollo','cordero','salmon','merluza','kebab','pizza1','pizza2','pizza3']
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza1','cerveza2']
lista_postres = ['helado','fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']
#Generar itmes comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0 

for comida in lista_comidas:
    #Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command = revisar_check())
    comida.grid(row=contador, 
                column=0, 
                sticky=W)
    #Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',19,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable= texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    
    contador +=1

#Generar itmes bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0 
for bebida in lista_bebidas:
    #Crear Checkbutton    
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command = revisar_check())
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    #Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis',19,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable= texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)    
    
    contador +=1

#Generar itmes comida
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0 

for postre in lista_postres:
    #Crear Checkbutton   
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command = revisar_check())

    postre.grid(row=contador, column=0, sticky=W)
    #Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis',19,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable= texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)       
    contador +=1

#Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


#Etiquetas de costo y campos de entrada 
#--------Comida-------------
etiqueta_costo_comida = Label(panel_costos,
                              text= 'Costo comida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)
#--------bebida-------------
etiqueta_costo_bebida = Label(panel_costos,
                              text= 'Costo bebida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)
#--------postre-------------
etiqueta_costo_postre = Label(panel_costos,
                              text= 'Costo postre',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1,padx=41)
#--------subtotal-------
etiqueta_subtotal = Label(panel_costos,
                              text= 'Subtotal',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)
#--------Impuesto-------
etiqueta_impuesto = Label(panel_costos,
                              text= 'Impuesto',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3,padx=41)
#-------Total----------
etiqueta_total = Label(panel_costos,
                              text= 'Total',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)

#Botones 
botones = ['total','recibo','guardar','resetear']
columnas = 0 
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    boton.grid(row=0,
               column=columnas)
    
    columnas +=1 

#Area de recibo 
texto_recibo = Text(panel_recibo,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=42,
                   height=10)                    
texto_recibo.grid(row=0,
                  column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadura,
                   font=('Dosis',16,'bold'),
                   bd=1,
                   width=42,)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       '=','Borrar','0','/']
botones_guardados = []

fila = 1
columna = 0 

for boton in botones_calculadora:
    boton = Button(panel_calculadura,
                   text=boton.title(),
                   font=('Dosis',16,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=10)
    
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila +=1
    
    columna +=1
    
    if columna == 4:
        columna = 0    
     
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))  
         
#Evitar que la pantalla se cierre 
aplicacion.mainloop()