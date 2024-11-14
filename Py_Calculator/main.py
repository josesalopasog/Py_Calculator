import tkinter as tk
import numpy as np 
from tkinter import ttk

#--Clase Frame: Se define un clase hija para el frame principal heredando los atributos de la clase padre 'tk.Frame' --
class MainFrame(tk.Frame):
    def __init__(self, master): 
        super().__init__(master) #Llamamos al contructor de la clase padre 'tk.Frame'
        self.result_state = False  # Nueva variable para rastrear si se muestra un resultado
        self.config(bg="#111111")
        self.create_visor() #Llamamos a los widgets configurados
        self.create_buttons()
    
    #Definimos un metodo para crear el visor que mostrara los numeros en el "Widget Maestro"    
    def create_visor(self):
        self.visor_text = tk.StringVar() #Construimos una variable String la cual sera la que se ve en el visor 
        self.visor = tk.Entry(self, #Creamos un widget de entrada 
                              bg = 'black', #Este parámetro defin el color del fondo del widget
                              fg = 'white', #Este parámetro define el color de la fuente del texto del widget 
                              textvariable=self.visor_text, #Definimos cual es el texto que aparecera en el widget
                              font=('Helvetica',32), #Este parámetro define el tipo de fuente y el tamaño de la fuente 
                              bd=10, #ste parámetro establece el grosor del borde del widget
                              insertwidth=4, #Este parámetro controla el grosor del cursor (la línea vertical que parpadea dentro del cuadro de texto)
                              width=14, #Este parámetro define el ancho del cuadro de texto en términos del número de caracteres que se pueden mostrar a la vez en la entrada.
                              borderwidth=2, 
                              justify='right', #Parametrizamos en que posición se comenzara a escribir el texto
                              relief='sunken') 
        #Definimos en que ubicación estara el visor
        self.visor.grid(row=0, 
                        column=0,
                        columnspan=4,
                        sticky='ew',
                        padx=10,
                        pady=10)
        self.expresion = '' #Ahora establecemos el texto inicial del visor el cual modificaremos despues cuando se oprime algún botón. 
    
    #Definimos un metodo para crear los botones que estaran en el widget maestro:    
    def create_buttons(self):
        #Creamos una lista de tuplas con el simbolo que aparecera en el botón y su ubicación en el grid. 
        botones_calculadora = [('%',1,0),('CE',1,1),('C',1,2),('«',1,3),         
                               ('1/x',2,0), ('x²',2,1),('²√x',2,2),('÷',2,3),
                               ('7',3,0), ('8',3,1), ('9',3,2), ('×',3,3), 
                               ('4',4,0), ('5',4,1), ('6',4,2), ('-',4,3),
                               ('1',5,0), ('2',5,1), ('3',5,2), ('+',5,3), 
                               ('±',6,0), ('0',6,1), (',',6,2), ('=',6,3)]
        
        #Ahora iteramos sobre la lista para que cree el boton según la lista de simbolos 
        for btext, r,c in botones_calculadora:
            tk.Button(self,
                      bg='#111111', #Este parámetro define el color del fondo del botón 
                      fg='white', #Este parámetro define el color del texto del botón
                      text=btext, #Este parámetro define el texto que aparecera en el botón 
                      padx=20, #Este parámetro establece el espacio horizontal de relleno del widget
                      pady=20, #Este parámetro establece el espacio vertical de relleno del widget
                      font=('Helveltica',20), #Este parámetro define el tipo de fuente y el tamaño del texto del widget 
                      command=lambda t=btext: self.click_button(t) #Este parametró define el comando que realizara el botón al ser oprimido. 
                                                                   #En este caso lamda funcióna para crear una función simple dentro de la misma linea, 
                                                                   # cuando lamda sea llamada en este caso al hacer clic en el botón, ejecutará el método self.click_button(t), pasando t como argumento.
                      #Definimos la ubicación de los botones según las tuplas que definimos arriba. 
                      ).grid(row=r,
                             column=c,
                             sticky='nsew') #Este parámetro controla hacia qué lados de la celda debe "adherirse" (stick) el widget. (n=north,s=south,e=east,w=west)
    
    #Definimos ahora el metodo que controlara que acción realizara según el botón que se oprima.
    def click_button(self, var_text):
                
        current_visor_text = self.visor_text.get() #Declaramos la variable current_visor_text para obtener el valor que esta actualmente en el visor
         
        if self.result_state and var_text in '0123456789': 
            self.visor_text.set(var_text)
            self.result_state = False
        else:
            self.result_state = False
            #En esta parte actualizaremos lo que esta actualmente en el visor sumando el valor del boton que el usuario escoja.
            if var_text in '0123456789': 
                self.visor_text.set(current_visor_text + var_text) 
            elif var_text in '+-': 
                self.visor_text.set(current_visor_text + ' ' + var_text + ' ')
            elif var_text == '×':
                self.visor_text.set(current_visor_text+' '+'*'+' ')
            elif var_text == '÷':
                self.visor_text.set(current_visor_text+' '+'/'+' ')
            elif var_text == 'C':
                self.visor_text.set('')
            elif var_text == '«':
                self.visor_text.set(current_visor_text[:-1])
            elif var_text == '±':
                current_value = float(current_visor_text)
                self.visor_text.set(str(-current_value))
            elif var_text == '²√x':
                current_value = float(current_visor_text)
                self.visor_text.set(str(round(np.sqrt(current_value),8)))
            elif var_text == '1/x':
                current_value = float(current_visor_text)
                self.visor_text.set(str(1 / current_value))
            elif var_text == 'x²':
                current_value = float(current_visor_text)
                self.visor_text.set(str(current_value ** 2))
            #Una vez actualizado el visor con las operaciones que quiere hacer el usuario con el botón '=' analizamos la operación que esta actualmente en el visor y lo remplazamos mostrando el resultado
            elif var_text == '=':
                try:
                    result = str(eval(current_visor_text)) #Evaluamos lo que esta actualmente en el visor con la función eval() y la guardamos en la variable resultado 
                    self.visor_text.set(result) #Por ultimo mostramos el resultado en el visor 
                    self.result_state = True
                except ZeroDivisionError: #Si despues de la evaluación hay alguna expresion con división por 0 muestra el error 
                    self.visor_text.set('Er:ZeroDivision')
                    self.result_state = True 
                except ValueError: #Si surge algún error inesperado mostrara error 
                    self.visor_text.set('Error')
                    self.result_state = True
 
#--Clase MainApp: Se define un clase hija para la ventana cprincipal de la aplicación heredando los atributos de la clase padre 'tk.Tk' --
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__() #Llamamos al contructor de la clase padre 'tk.Tk'
        #--Ahora con los atributos que tiene 'tk.Tk' definimos la estetica de la ventana-- 
        self.title('Calculadora') #Declaramos el titulo de la App
        self.config(bg="#111111") #Configuramos el color del fondo del frame 
        self.resizable(False, False)  # Deshabilitamos el redimensionamiento de la ventana
        self.iconbitmap('C:\\Users\\Usuario\\Documents\\Py_Calculadora\\icon_calculadora.ico') #Cambiamos el icono de la app.
        self.config_grid()
        self.show_frame()

    def config_grid(self):
        for i in range(4):
            self.grid_columnconfigure(i,weight=1)
        for i in range(6):
            self.grid_rowconfigure(i,weight=1)   

    #Definimos un metodo para mostrar los widgets dentro del Frame     
    def show_frame(self):
        frame = MainFrame(self)
        frame.grid(column=0,row=0,sticky='ew')
    
app = MainApp()
app.mainloop()