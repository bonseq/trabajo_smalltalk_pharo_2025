import numpy as np
import tkinter as tk

class Tablero:
    def __init__(self, n):
        self.n = n
        self.APA = 0  # muerto
        self.ENC = 1  # vivo
        self.grilla = np.full((n, n), self.APA)

    def contar_vecinos(self, i, j):
        n = self.n
        g = self.grilla
        total = int(
            g[i, (j - 1) % n] + g[i, (j + 1) % n] +
            g[(i - 1) % n, j] + g[(i + 1) % n, j] +
            g[(i - 1) % n, (j - 1) % n] + g[(i - 1) % n, (j + 1) % n] +
            g[(i + 1) % n, (j - 1) % n] + g[(i + 1) % n, (j + 1) % n]
        )
        return total

    def actualizar(self):
        nueva = self.grilla.copy()
        for i in range(self.n):
            for j in range(self.n):
                total = self.contar_vecinos(i, j)
                if self.grilla[i, j] == self.ENC:
                    if total < 2 or total > 3:
                        nueva[i, j] = self.APA
                else:
                    if total == 3:
                        nueva[i, j] = self.ENC
        self.grilla = nueva

    def limpiar(self):
        self.grilla = np.full((self.n, self.n), self.APA)

    def toggle_celda(self, i, j):
        #cambia el estado de una celda (viva/muerta)
        self.grilla[i, j] = self.ENC if self.grilla[i, j] == self.APA else self.APA

class JuegoGUI:
    def __init__(self, raiz, tablero):
        self.raiz = raiz
        self.tablero = tablero
        self.running = False
        self.velocidad = 200  # milisegundos entre frames
        self.botones = []
        self.crear_interfaz()

    def crear_interfaz(self):
        #crea la grilla de botones y los controles
        for i in range(self.tablero.n):
            fila = []
            for j in range(self.tablero.n):
                b = tk.Button(
                    self.raiz,
                    width=4, height=2,
                    bg='white'if [i,j] else 'white',
                    command=lambda i=i, j=j: self.toggle(i, j)
                )
                b.grid(row=i, column=j, sticky="nsew")
                fila.append(b)
            self.botones.append(fila)

        # botones de control
        tk.Button(self.raiz, text='Comenzar', command=self.comenzar).grid(row=self.tablero.n, column=0)
        tk.Button(self.raiz, text='Parar', command=self.parar).grid(row=self.tablero.n, column=1)
        tk.Button(self.raiz, text='Paso', command=self.paso).grid(row=self.tablero.n, column=2)
        tk.Button(self.raiz, text='Limpiar', command=self.limpiar).grid(row=self.tablero.n, column=3)

        # menu de velocidad
        tk.Label(self.raiz, text="Velocidad:").grid(row=self.tablero.n, column=4)
        self.opcion = tk.StringVar(self.raiz)
        self.opcion.set("Normal")
        opciones = {"Lento": 500, "Normal": 200, "Rápido": 50}
        menu = tk.OptionMenu(self.raiz, self.opcion, *opciones.keys(), command=self.cambiar_velocidad)
        menu.grid(row=self.tablero.n, column=5)

    def toggle(self, i, j):
        self.tablero.toggle_celda(i, j)
        self.actualizar_vista()

    def comenzar(self):
        self.running = True
        self.correr()

    def parar(self):
        self.running = False

    def paso(self):
        self.tablero.actualizar()
        self.actualizar_vista()

    def limpiar(self):
        self.running = False
        self.tablero.limpiar()
        self.actualizar_vista()

    def correr(self):
        if self.running:
            self.tablero.actualizar()
            self.actualizar_vista()
            self.raiz.after(self.velocidad, self.correr)

    def actualizar_vista(self):
        for i in range(self.tablero.n):
            for j in range(self.tablero.n):
                color = 'black' if self.tablero.grilla[i, j] else 'white'
                self.botones[i][j].config(bg=color)

    def cambiar_velocidad(self, seleccion):
        velocidades = {"Lento": 500, "Normal": 200, "Rápido": 50}
        self.velocidad = velocidades.get(seleccion, 200)


if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Juego de la Vida - Conway")
    tablero = Tablero(10)
    juego = JuegoGUI(raiz, tablero)
    raiz.mainloop()