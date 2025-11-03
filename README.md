# 🧬 Juego de la Vida – Conway

Una implementación del **Juego de la Vida de John Conway** desarrollada en **Python 🐍** utilizando **Tkinter** para la interfaz gráfica y **NumPy** para el manejo eficiente de la grilla. Y luego en **Smalltalk🗣️** ##Agregar las dependencias

Este proyecto forma parte del trabajo práctico de la cátedra **Paradigmas de Programación**, modelado bajo los principios de la **Programación Orientada a Objetos (POO)**.

---

## 🧠 Descripción del juego

El **Juego de la Vida** es un autómata celular donde cada celda del tablero puede estar en uno de dos estados:
- 🟩 **Viva**
- ⬜ **Muerta**

Su evolución depende del estado de sus 8 celdas vecinas y sigue las siguientes reglas:

1. Una célula viva con menos de 2 vecinas vivas 🪦 **muere por soledad**.  
2. Una célula viva con 2 o 3 vecinas vivas 💚 **sobrevive**.  
3. Una célula viva con más de 3 vecinas vivas 🔥 **muere por sobrepoblación**.  
4. Una célula muerta con exactamente 3 vecinas vivas 🌱 **revive**.

---

### 🧱 Clases principales (🐍)

| Clase | Rol | Descripción |
|--------|-----|-------------|
| **Tablero** | Modelo | Contiene la grilla y aplica las reglas de evolución. |
| **JuegoGUI** | Vista/Controlador | Conecta la lógica con la interfaz Tkinter. |

### 🧱 Clases principales (🗣️)

| Clase | Rol | Descripción |
|--------|-----|-------------|
| **Tablero** | Modelo | Contiene la grilla y aplica las reglas de evolución. |
| **JuegoGUI** | Vista/Controlador | Conecta la lógica con la interfaz Tkinter. |


---

## 🚀 Ejecución
### 1️⃣ Cloná el repositorio
### 2 Instala requerimientos (tkinter y numpy)

🧭 Próximos pasos / Ideas futuras

🖼️ Añadir soporte para guardar y cargar patrones.

🌈 Permitir elegir colores personalizados

📐 Arreglar tamaño del tablero para que queden botones parejos

🧩 Realizar el modelo a Pharo Smalltalk como ejercicio comparativo de paradigma.

👩‍💻 Autores

Bonguan Juliana, Centurion Constanza, Sanchez Romina, Teruel Axel  – UTN FRRe
Catedra Paradigmas de Programación.







