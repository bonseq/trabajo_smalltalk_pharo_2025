import tkinter as tk
import numpy as np
from juego_de_la_vida import actualizar, grilla, n, APA, ENC


raiz = tk.Tk()


raiz.grid_columnconfigure(0, weight=1)
raiz.grid_rowconfigure(0, weight=1)
raiz.resizable(0, 0)
buttons=[]


def clicki(i, j, grilla, buttons):
    grilla[i,j] = 1 if grilla[i,j]==0 else 0
    buttons[i][j].config(bg='black' if grilla[i,j] else 'white')


for i in range(n):
    row=[]
    for j in range (n):
        button=tk.Button(
            raiz,
            command= lambda i=i, j=j: clicki(i, j , grilla,buttons),
            height=2,
            width=4,
            bg= 'black' if grilla[i,j] else 'white'
        )
        row.append(button)
    buttons.append(row)


for i in range(n):
    for j in range(n):
        buttons[i][j].grid(row=i, column=j, sticky="nsew")
#botoncitos
botonComenzar = tk.Button(raiz, text='Comience')
botonComenzar.grid(row=n, column = 0, columnspan=n//5, sticky="we")
botonPare = tk.Button(raiz, text='Parar')
botonPare.grid(row=n, column = n//5, columnspan=n//5, sticky="we")
botonSteps = tk.Button(raiz, text='Steps')
botonSteps.grid(row=n, column = 4, columnspan=n//5, sticky="we")
botonClear = tk.Button(raiz, text='Clear')
botonClear.grid(row=n, column = 6, columnspan=n//5, sticky="we")

        
#ESTE PATRON SE MANDA AL BACKEND
raiz.mainloop()