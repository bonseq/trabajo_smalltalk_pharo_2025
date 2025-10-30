import tkinter as tk
import numpy as np
from juego_de_la_vida import actualizar, grid, n, APA, ENC


raiz = tk.Tk() #raiz es la ventanita que se abre, tk.Tk() la


raiz.grid_columnconfigure(0, weight=1)
raiz.grid_rowconfigure(0, weight=1)
raiz.resizable(0, 0)
buttons=[]


def clicki(i, j, grid, buttons):
    grid[i,j] = 1 if grid[i,j]==0 else 0
    buttons[i][j].config(bg='black' if grid[i,j] else 'white')


for i in range(n):
    row=[]
    for j in range (n):
        button=tk.Button(
            raiz,
            command= lambda i=i, j=j: clicki(i, j , grid,buttons),
            height=2,
            width=4,
            bg= 'black' if grid[i,j] else 'white'
        )
        row.append(button)
    buttons.append(row)


for i in range(n):
    for j in range(n):
        buttons[i][j].grid(row=i, column=j, sticky="nsew")

#interaccion con la lofica
def gui_backend():
    global grid
    grid=actualizar(grid)
    for i in range(n):
        for j in range(n):
            buttons[i][j].config(bg= 'black' if grid[i,j] else 'white')


def correr():
    global grid
    if running:
        grid = actualizar(grid)
        for i in range(n):
            for j in range(n):
                buttons[i][j].config(bg='black' if grid[i, j] else 'white')
        raiz.after(200, correr)  # vuelve a llamarse cada 200 ms

def Comience():
    global running
    running=True
    correr()
#    gui_backend()

def pasos():
    global running
    running=True
    gui_backend()

def parar():
    global running
    running=False


def limpiar():
    global grid, running
    running=False
    grid=np.full((n,n), APA)
    for i in range(n):
        for j in range(n):
            buttons[i][j].config(bg='white')


#botoncitos
botonComenzar = tk.Button(raiz, text='Comience', command= lambda:Comience())
botonComenzar.grid(row=n, column = 0, columnspan=n//5, sticky="we")

# # botonPare = tk.Button(raiz, text='Parar', command=lambda:parar())
# # botonPare.grid(row=n, column =1, columnspan=n//5, sticky="we")

# # botonSteps = tk.Button(raiz, text='Steps', command= lambda:pasos())
# # botonSteps.grid(row=n, column = 3, columnspan=n//5, sticky="we")

# # botonClear = tk.Button(raiz, text='Clear', command=lambda:limpiar())
# # botonClear.grid(row=n, column = 4, columnspan=n//5, sticky="we")

# # running=False #para difeerenciar step de comience

raiz.mainloop()