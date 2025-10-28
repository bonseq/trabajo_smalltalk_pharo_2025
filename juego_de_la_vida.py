import numpy as np

n=10
ENC=1
APA=0

grilla=np.full((n,n),APA) ##recibe el patron que genere

def actualizar(grilla):
    newGrilla=grilla.copy()  #copia el patron
    for i in range(n):
        for j in range(n):
            total= int(grilla[i, (j-1)%n]+ grilla[i,(j+1)%n]+           #accede a las 8 celdad
                    grilla[(i-1)%n, j]+ grilla[(i+1)%n, j]+             #cuanta cuantas celulas vivas hay accediendo a los 8 lugares al rededor de la celula
                    grilla[(i-1)%n, (j-1)%n]+ grilla[(i-1)%n, (j+1)%n]+ #ocupando modulo % podemos hacer que el tablero sea logico
                    grilla[(i+1)%n, (j-1)%n]+ grilla[(i+1)%n, (j+1)%n])    
            if grilla[i, j] == ENC:
                if (total<2) or (total>3):      #apllica reglas a la celda para matarla o revivirla
                    #matarla
                    newGrilla[i, j] == APA
            else:
                if total == 3:
                    newGrilla[i,j] == ENC
    return newGrilla

print(grilla)