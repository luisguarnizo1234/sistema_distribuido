#!/usr/bin/python
import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
import matplotlib
matplotlib.use('TkAgg')


import datetime as dt
import matplotlib.pyplot as plt

#libreria par colocar graficos de matplotlib en un canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

#grafico en tiempo real
import matplotlib.animation as animation
import sqlite3
from matplotlib import style
style.use('ggplot')
from matplotlib.figure import Figure



root = Tk.Tk()
root.wm_title("Embedding in TK")


f = plt.Figure(figsize=(10, 6), dpi=100)
a = f.add_subplot(521)
#a1 = f.add_subplot(312)
a1 = f.add_subplot(522)
a2 = f.add_subplot(525)
a3 = f.add_subplot(526)


canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



#función para animar la grafica
def animate(i):
   
    dbObj = DatabaseManager()

    y1 = dbObj.consulta("select rssi from tabla1 ORDER BY id DESC LIMIT 10")
    y2 = dbObj.consulta("select rssi from tabla2 ORDER BY id DESC LIMIT 10")
    y3 = dbObj.consulta("select rssi from tabla3 ORDER BY id DESC LIMIT 10")
    y4 = dbObj.consulta("select rssi from tabla4 ORDER BY id DESC LIMIT 10")
    
    r1 = dbObj.consulta("select ruido from tabla1 ORDER BY id DESC LIMIT 10")
    r2 = dbObj.consulta("select ruido from tabla2 ORDER BY id DESC LIMIT 10")
    r3 = dbObj.consulta("select ruido from tabla3 ORDER BY id DESC LIMIT 10")
    r4 = dbObj.consulta("select ruido from tabla4 ORDER BY id DESC LIMIT 10")
   
    #invertir los datos para que aparezcan en orden de llegada
    y11 = y1[::-1]
    y12 = y2[::-1]
    y13 = y3[::-1]
    y14 = y4[::-1]
    print('Y1:')
    print(y1)
    
    r11 = r1[::-1]
    r12 = r2[::-1]
    r13 = r3[::-1]
    r14 = r4[::-1]
    print('Y1:')
    print(y1)
    
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b1 =  dbObj.consulta("select hora from tabla1 ORDER BY id DESC LIMIT 10")
    b2 =  dbObj.consulta("select hora from tabla2 ORDER BY id DESC LIMIT 10")
    b3 =  dbObj.consulta("select hora from tabla3 ORDER BY id DESC LIMIT 10")
    b4 =  dbObj.consulta("select hora from tabla4 ORDER BY id DESC LIMIT 10")
    #labels = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
       
    print(x)

    print('d:')
    dates11 = b1[::-1]
    dates12 = b2[::-1]
    dates13 = b3[::-1]
    dates14 = b4[::-1]
    a.clear()
    a.plot(x, y11, "#00A3E0", label="RSSI")
    a.plot(x, r11, "#FF3C33", label="Ruido")
   
   
    #colocar fecha
    plt.setp(a.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    a.set_xticks(x)
    a.set_xticklabels(dates11)
   
    #información de la grafica
    a.set_ylabel('Señal(dBm)')
    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=4, borderaxespad=0)
    title = "             Nodo 1 "
    a.set_title(title)
    
    #grafico 2_________________________________________________________________
    a1.clear()
    a1.plot(x, y12, "#00A3E0", label="RSSI")
    a1.plot(x, r11, "#FF3C33", label="Ruido")
    
    plt.setp(a1.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    a1.set_xticks(x)
    a1.set_xticklabels(dates12)
   
    #información de la grafica
    a1.set_ylabel('Señal(dBm)')
    a1.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=4, borderaxespad=0)
    title = "             Nodo 2"
    a1.set_title(title)
    
    #grafico 3_________________________________________________________________
    a2.clear()
    a2.plot(x, y13, "#00A3E0", label="RSSI")
    a2.plot(x, r11, "#FF3C33", label="Ruido")
    
    plt.setp(a2.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    a2.set_xticks(x)
    a2.set_xticklabels(dates13)
   
    #información de la grafica
    a2.set_ylabel('Señal(dBm)')
    a2.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=4, borderaxespad=0)
    title = "             Nodo 3"
    a2.set_title(title)
    
    #grafico 4_________________________________________________________________
    a3.clear()
    a3.plot(x, y14, "#00A3E0", label="RSSI")
    a3.plot(x, r11, "#FF3C33", label="Ruido")
    
    plt.setp(a3.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    a3.set_xticks(x)
    a3.set_xticklabels(dates14)
   
    #información de la grafica
    a3.set_ylabel('Señal(dBm)')
    a3.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=4, borderaxespad=0)
    title = "             Nodo 4"
    a3.set_title(title)
    
    
    
    plt.show()
    del dbObj
   
   
# Database Manager Class
class DatabaseManager():
    def __init__(self):
        self.conexion = sqlite3.connect(DB_Name)
        self.conexion.execute('pragma foreign_keys = on')
        self.conexion.commit()
        self.cursor = self.conexion.cursor()
    
    def add_del_update_db_record(self, sql_query, args=()):
        self.cursor.execute(sql_query, args)
        self.conexion.commit()
        return
    
    def __del__(self):
        self.cursor.close()
        self.conexion.close()
           
        #Metodo para consultar datos de la base de datos
    def consulta(self, sql_query):
        self.cursor.execute(sql_query)
        row= self.cursor.fetchall()
        #print (row[0])
        self.conexion.commit()
        return(row)


# SQLite DB Name
DB_Name =  "datos2.db"
button = Tk.Button(master=root, text='Quit', command=_quit)

button.pack(side=Tk.BOTTOM)
ani = animation.FuncAnimation(f, animate, interval=500)
Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.